from app import app
from db import db

db.init(app)

@app.before_first_request #run method before first request.
def create_table():
    db.create_all()
