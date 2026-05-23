AnimeForUs

AnimeForUs is a dynamic web application that allows users to explore, search, and view anime content. It fetches real-time data using the Jikan API and provides categorized anime like trending, popular, and genre-based listings.


Features
    1. Search anime by name
    2. Anime viewing interface (UI-based player)
    3. Trending & Popular anime sections
    4. Browse anime by genres (Action, Comedy, Romance, etc.)
    5. Latest and Upcoming anime
    6. User authentication (Login/Register)
    7. Detailed anime information pages
    8. Comment system



Tech Stack
    Backend:  Flask (Python)
    Forntend :  HTML, CSS, JavaScript
    DB : SQLite
    API : Jikan API (MyAnimeList Unofficial API)

Project Structure
AnimeForUs/
│
├── static/ # CSS, JS, Images
├── templates/ # HTML templates
├── fetch_data.py # API handling functions
├── models.py # Database models
├── routes.py # Application routes
├── app.py # Main Flask app
├── requirements.txt # Dependencies
├── .env # Environment variables (ignored)
└── README.md


Installation & Setup

Clone the repository

git clone https://github.com/YOUR_USERNAME/AnimeForUs.git
cd AnimeForUs

Create virtual environment
    python -m venv venv
    venv\Scripts\activate   # For Windows#

Install dependencies
    pip install -r requirements.txt

Create .env file
    SECRET_KEY=your_secret_key_here

Run the application
    python route.py

API Used
    Jikan API (https://jikan.moe/)
    Provides anime data without requiring an API key

Limitations
    This application does not support real anime streaming.
    It uses the Jikan API, which only provides anime metadata (titles, images, descriptions).
    Video playback features are for UI demonstration purposes only.

Future Scope
    Integrate legal anime streaming sources (if available)
    Add caching for faster API responses
    Improve user profile system
    Enhance UI/UX design
    Deploy project online

Security
    Sensitive data like SECRET_KEY is stored in .env
    .env is excluded using .gitignore



