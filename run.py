from app import app
from db import db

dp.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()