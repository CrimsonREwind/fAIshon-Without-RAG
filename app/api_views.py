import os
import re
import json
import base64
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from groq import Groq

# Import our lightweight LangChain AI service
from .ai_service import get_upcycle_ideas, get_instructions

@login_required
def generate_ideas(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    try:
        # Get the files from the request (front, back, closeup)
        front_file = request.FILES.get('front')
        back_file = request.FILES.get('back')
        closeup_file = request.FILES.get('closeup')
        if not (front_file and back_file and closeup_file):
            return JsonResponse({'error': 'Missing one or more required images (front, back, closeup).'}, status=400)
        # Convert images to base64 strings
        def file_to_b64(f):
            mime_type = getattr(f, "content_type", "image/jpeg")
            b64 = base64.b64encode(f.read()).decode('utf-8')
            return f"data:{mime_type};base64,{b64}"
        b64_front = file_to_b64(front_file)
        b64_back = file_to_b64(back_file)
        b64_closeup = file_to_b64(closeup_file)
        # Groq API setup
        api_key = os.environ.get("GROQ_API_KEY", "")
        if not api_key:
            return JsonResponse({'error': 'Groq API Key is missing on the server.'}, status=500)
        client = Groq(api_key=api_key)

        # ============================================================
        # STEP 1: Use Groq Vision to analyze the garment images
        # (We still do this directly with Groq because we need to send
        # images, and LangChain's Groq integration doesn't handle
        # multi-image vision calls as cleanly)
        # ============================================================
        system_prompt = """
        You are a sustainable fashion AI expert.
        Analyze the provided images of an old garment (Front, Back, Closeup).
        Extract technical details about the garment.
        You MUST respond ONLY with valid JSON in the exact format shown below, with no markdown code blocks wrapping it:
        {
          "garment_type": "T-Shirt",
          "subcategory": "Graphic Tee",
          "primary_color": "Blue",
          "secondary_colors": ["White", "Red"],
          "fabric_type": "Cotton blend",
          "pattern": "Solid with print",
          "fit": "Regular",
          "sleeve_length": "Short",
          "seasonality": ["Summer", "Spring"],
          "estimated_reusability_score": 85,
          "confidence": 0.95
        }
        """
        content_list = [
            {"type": "text", "text": system_prompt + "\n\nBased on these 3 images (Front, Back, Closeup details), generate the technical garment analysis in the requested JSON format."},
            {"type": "image_url", "image_url": {"url": b64_front}},
            {"type": "image_url", "image_url": {"url": b64_back}},
            {"type": "image_url", "image_url": {"url": b64_closeup}}
        ]
        completion = client.chat.completions.create(
            model="qwen/qwen3.8-27b",
            messages=[
                {
                    "role": "user",
                    "content": content_list
                }
            ],
            temperature=0.60,
            max_completion_tokens=800,
            top_p=0.95,
            stream=False,
        )
        ai_message = completion.choices[0].message.content or ""
        # Extract the JSON object gently
        ai_message_clean = re.sub(r'```json', '', ai_message)
        ai_message_clean = re.sub(r'```', '', ai_message_clean)
        match = re.search(r'\{.*\}', ai_message_clean, re.DOTALL)
        if not match:
            return JsonResponse({'error': 'AI response did not contain a valid JSON object.', 'raw': ai_message}, status=500)
        clean_json = match.group(0).strip()
        garment_analysis = json.loads(clean_json)

        # ============================================================
        # STEP 2: Use lightweight LangChain chain to generate upcycle concepts
        # Fast, zero-RAM, cloud-based via Groq API
        # ============================================================
        garment_description = (
            f"Garment type: {garment_analysis.get('garment_type', 'Unknown')}. "
            f"Fabric: {garment_analysis.get('fabric_type', 'Unknown')}. "
            f"Color: {garment_analysis.get('primary_color', 'Unknown')}. "
            f"Pattern: {garment_analysis.get('pattern', 'Unknown')}. "
            f"Fit: {garment_analysis.get('fit', 'Unknown')}. "
            f"Condition/reusability score: {garment_analysis.get('estimated_reusability_score', 'N/A')}."
        )

        print(f"[API] Garment analyzed: {garment_analysis.get('garment_type')} - {garment_analysis.get('fabric_type')}")
        print(f"[API] Querying LangChain chain for upcycle ideas...")

        ai_response = get_upcycle_ideas(garment_description)

        # Parse the AI response (it should be JSON)
        ai_clean = re.sub(r'```json', '', ai_response, flags=re.IGNORECASE)
        ai_clean = re.sub(r'```', '', ai_clean)
        match_concepts = re.search(r'\{.*\}', ai_clean, re.DOTALL)

        if match_concepts:
            concepts_data = json.loads(match_concepts.group(0).strip())
            # Merge the garment analysis with the concepts
            garment_analysis["concepts"] = concepts_data.get("concepts", [])
        else:
            print(f"[API] Warning: AI response wasn't valid JSON, returning analysis only")
            garment_analysis["concepts"] = []

        return JsonResponse(garment_analysis, status=200)

    except json.JSONDecodeError as e:
        return JsonResponse({'error': f'Failed to parse AI response as JSON: {str(e)}'}, status=500)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=500)

@login_required
def generate_instructions(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    try:
        body = json.loads(request.body)
        concept_title = body.get('title')
        concept_desc = body.get('description')
        garment_info = body.get('garment_info', {})
        if not concept_title or not concept_desc:
            return JsonResponse({'error': 'Missing concept title or description.'}, status=400)

        # ============================================================
        # Use lightweight LangChain chain to generate DIY instructions
        # Fast, zero-RAM, cloud-based via Groq API
        # ============================================================
        print(f"[API] Generating instructions for: {concept_title}")
        print(f"[API] Querying LangChain chain for instructions...")

        ai_response = get_instructions(
            concept_title, concept_desc, garment_info
        )

        # Parse the response JSON
        ai_clean = re.sub(r'```json', '', ai_response, flags=re.IGNORECASE)
        ai_clean = re.sub(r'```', '', ai_clean)
        match = re.search(r'\{.*\}', ai_clean, re.DOTALL)

        if not match:
            return JsonResponse({'error': 'AI response did not contain valid JSON.', 'raw': ai_response}, status=500)

        instructions_result = json.loads(match.group(0).strip())
        return JsonResponse(instructions_result, status=200)

    except json.JSONDecodeError as e:
        return JsonResponse({'error': f'Failed to parse JSON: {str(e)}'}, status=500)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=500)
