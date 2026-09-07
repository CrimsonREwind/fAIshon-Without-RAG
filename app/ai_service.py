"""
ai_service.py
-------------------------------------------------------
Lightweight LangChain AI service for fAIshon.

Replaces the heavy pgvector/PyTorch/sentence-transformers RAG pipeline
with a fast, direct LangChain ChatGroq chain.

Key benefits:
- Zero local machine learning model downloads (no PyTorch, no HuggingFace models)
- Minimal RAM usage (~0MB extra), perfectly suited for free-tier servers (512MB RAM)
- Sub-second responses directly via Groq cloud API
- Retains rich domain guidance via structured prompt engineering
-------------------------------------------------------
"""

import os
import re
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def get_llm():
    """Create and return a lightweight LangChain ChatGroq client."""
    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in environment variables.")

    model_name = os.environ.get("GROQ_MODEL", "qwen/qwen3.8-27b")
    return ChatGroq(
        api_key=api_key,
        model=model_name,
        temperature=0.6,
        max_tokens=800,
    )


def clean_json_text(text: str) -> str:
    """Extract raw JSON text by stripping markdown fences if present."""
    if not text:
        return "{}"
    cleaned = re.sub(r'```json', '', text, flags=re.IGNORECASE)
    cleaned = re.sub(r'```', '', cleaned)
    match = re.search(r'\{.*\}', cleaned, re.DOTALL)
    if match:
        return match.group(0).strip()
    return cleaned.strip()


def get_upcycle_ideas(garment_analysis_text: str) -> str:
    """
    Given garment analysis attributes, generate exactly 3 creative,
    feasible upcycling concepts (Easy, Medium, Hard) using LangChain.

    Returns a JSON string matching the frontend schema.
    """
    system_prompt = """You are an expert sustainable fashion designer and master tailor.
Your goal is to suggest 3 creative, feasible, and stylish upcycling concepts based on the analyzed garment.

Domain Expertise to apply:
- Cotton / T-shirts: Easy to cut, sew, and dye. Great for totes, crop tops, patchwork, yarn, and layered items.
- Denim / Heavy Twill: Sturdy and durable. Excellent for tote bags, bucket hats, utility vests, pouches, and reinforced patchwork.
- Wool / Knits: Requires stretch stitches or ballpoint needles; can be felted in hot water for non-fraying crafts.
- Synthetics / Polyester: Use low iron heat; resistant to fraying; great for linings, active accessories, and zip pouches.
- Silk / Delicates: Use fine needles and French seams; ideal for hair scrunchies, pocket squares, and accents.

Difficulty Guidelines:
- Easy: Basic cutting, no-sew or simple hand/straight stitches (e.g. tote bag, crop top, raw-edge patches).
- Medium: Involves hemming, adding straps, basic tailoring, or simple pattern alterations.
- Hard: Full deconstruction, structured accessories (e.g. bucket hat, lined jacket, complex patchwork).

You MUST respond ONLY with a valid JSON object in this exact schema (no markdown formatting, no backticks):
{{
  "concepts": [
    {{
      "title": "Short Descriptive Title",
      "difficulty": "Easy",
      "description": "Clear explanation of the concept, including what sections of the garment to reuse and how."
    }},
    {{
      "title": "Short Descriptive Title",
      "difficulty": "Medium",
      "description": "Clear explanation of the concept, including what sections of the garment to reuse and how."
    }},
    {{
      "title": "Short Descriptive Title",
      "difficulty": "Hard",
      "description": "Clear explanation of the concept, including what sections of the garment to reuse and how."
    }}
  ]
}}
Ensure 'difficulty' is strictly one of: Easy, Medium, Hard.
"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "Garment Analysis:\n{garment_analysis}\n\nGenerate 3 distinct upcycling concepts.")
    ])

    llm = get_llm()
    chain = prompt | llm | StrOutputParser()
    raw_output = chain.invoke({"garment_analysis": garment_analysis_text})
    return clean_json_text(raw_output)


def get_instructions(concept_title: str, concept_desc: str, garment_info: dict) -> str:
    """
    Given a selected upcycling concept and garment metadata,
    generate detailed, step-by-step DIY tutorial instructions.

    Returns a JSON string matching the frontend schema.
    """
    garment_type = garment_info.get("garment_type", "garment")
    fabric_type = garment_info.get("fabric_type", "fabric")
    primary_color = garment_info.get("primary_color", "material")

    system_prompt = """You are a master tailor, pattern-maker, and sustainable fashion instructor.
Write a clear, practical, and beginner-friendly DIY upcycling guide for the user's project.

Tailoring Best Practices to apply:
- Provide accurate tools tailored to the fabric (e.g. heavy-duty needle size 16 for denim, ballpoint for knits, fabric scissors).
- Break instructions into logical, sequential steps (measuring/marking -> cutting -> pinning/ironing -> stitching -> finishing).
- Provide a practical 'pro_tip' regarding tension, needle choice, seam allowances, or finishing touches.

You MUST respond ONLY with a valid JSON object in this exact schema (no markdown formatting, no backticks):
{{
  "tools_needed": ["Tool 1", "Tool 2", "Tool 3", "Tool 4"],
  "estimated_time_minutes": 90,
  "instructions": [
    "Step 1: Description of preparation, measuring, and marking cutting lines.",
    "Step 2: Description of cutting along marked lines.",
    "Step 3: Description of pressing or pinning.",
    "Step 4: Description of sewing and assembly.",
    "Step 5: Description of finishing details, hems, or hardware."
  ],
  "pro_tip": "One high-value tailoring tip specifically relevant to this fabric and project."
}}
"""

    user_message = f"""Garment Details:
- Type: {garment_type}
- Fabric: {fabric_type}
- Color: {primary_color}

Selected Upcycle Project:
- Title: {concept_title}
- Description: {concept_desc}

Generate the complete DIY tutorial in JSON format."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", user_message)
    ])

    llm = get_llm()
    chain = prompt | llm | StrOutputParser()
    raw_output = chain.invoke({})
    return clean_json_text(raw_output)
