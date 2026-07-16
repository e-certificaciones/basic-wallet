## Setup

1. Create a virtualenv and install dependencies:
   `pip install -r requirements.txt`
2. Set a `SECRET_KEY` in `.env`
3. Run:
   `flask --app run.py run` 
   or 
   `python run.py`
4. Database:
   `python -m sqlite3 wallet.db`