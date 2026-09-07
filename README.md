# fAIshon — AI-Powered Sustainable Fashion Platform

This is my BCA final year project. The idea behind fAIshon is pretty simple — instead of throwing away old clothes, why not upcycle them into something new? The app uses AI to analyze garments and suggest creative upcycling ideas, and there's a whole community and marketplace built around sustainable fashion.

## What It Does

- **AI Upcycle Studio** — You upload 3 photos of an old garment (front, back, close-up), and the AI analyzes the fabric, color, condition etc. and gives you 3 upcycling ideas. You can then pick one and get full step-by-step instructions.
- **Community Feed** — Users can share their upcycling projects, like and comment on each other's posts. It's like a mini social media just for sustainable fashion.
- **Donation System** — You can donate old clothes either by dropping them off or scheduling a pickup. Based on the condition of the clothes, you earn coins.
- **Marketplace** — The coins you earn from donations can be used to buy upcycled fashion products from the marketplace.
- **Order Tracking** — Track all your marketplace purchases.
- **User Profiles & Settings** — Manage your profile, addresses, profile picture etc.

## Tech Stack

- **Backend** — Django 5.2, Python 3.11
- **Database** — SQLite (just for development, can switch to PostgreSQL for production)
- **AI** — Groq API with Llama 4 Scout model for garment analysis and instruction generation
- **Media Storage** — Cloudinary (all user uploads go here)
- **Production Server** — Gunicorn
- **Frontend** — Django templates with vanilla CSS and JavaScript

## Project Structure

```
final-project/
├── app/                    # Main application (views, models, urls, api)
│   ├── models.py           # All models - UserProfile, Post, Donation, Order etc.
│   ├── views.py            # Page views for auth, community, donation, marketplace
│   ├── api_views.py        # AI endpoints for garment analysis
│   ├── ai_service.py       # Lightweight LangChain chains (ChatGroq)
│   ├── urls.py             # All URL routes
│   ├── admin.py            # Admin panel setup
│   └── context_processors.py
├── core/                   # Django project config
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── templates/              # All HTML templates
├── static/                 # CSS, JS, images
├── media/                  # Local uploads (dev only)
├── assets/                 # collectstatic output
├── manage.py
├── requirements.txt
├── example.env             # Sample environment variables
```

## How to Set Up

### Requirements

- Python 3.11 or higher
- A Cloudinary account (free tier is fine) — [cloudinary.com](https://cloudinary.com/)
- A Groq API key — [console.groq.com](https://console.groq.com/)

### Steps

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/faishon.git
   cd faishon
   ```

2. **Create a virtual environment and activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate        # on Linux/Mac
   # venv\Scripts\activate          # on Windows
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp example.env .env
   ```
   Then open `.env` and put in your actual API keys:

   | Variable | What it is |
   |---|---|
   | `CLOUDINARY_CLOUD_NAME` | Your Cloudinary cloud name |
   | `CLOUDINARY_API_KEY` | Cloudinary API key |
   | `CLOUDINARY_API_SECRET` | Cloudinary API secret |
   | `GROQ_API_KEY` | Your Groq API key |

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Create a superuser** (if you want access to the admin panel)
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the server**
   ```bash
   python manage.py runserver
   ```
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and you're good to go.

## API Endpoints

These are the two AI-powered endpoints. Both need the user to be logged in.

| Method | URL | What it does |
|---|---|---|
| POST | `/api/generate/` | Takes 3 garment images, returns AI analysis + 3 upcycle ideas |
| POST | `/api/instructions/` | Takes a selected concept, returns detailed step-by-step tutorial |

## How the Coin System Works

When you donate clothes, you earn coins based on the condition:

| Condition | Coins per item |
|---|---|
| Like New | 20 |
| Good | 15 |
| Fair | 10 |
| Needs Repair | 5 |

These coins can then be spent in the marketplace to buy upcycled products.

## Deployment

For production, you'd want to:

1. Set `DEBUG = False` in `settings.py`
2. Use a proper `SECRET_KEY` (store it in `.env`)
3. Update `ALLOWED_HOSTS` with your domain
4. Run `python manage.py collectstatic`
5. Use Gunicorn to serve the app:
   ```bash
   gunicorn core.wsgi:application --bind 0.0.0.0:8000
   ```

I used Render for hosting during the demo, but Railway or any VPS with Nginx would work too.

