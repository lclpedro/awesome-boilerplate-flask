import os
from flask_pymongo import MongoClient

def get_db():
    HOST = os.environ.get('DB_HOST')
    PORT = os.environ.get('DB_PORT')
    conn = MongoClient(HOST, int(PORT))

    #Nome do banco de dados ficou survey_business.
    db = conn.database_name
    return db

def configure(app):
    app.db = get_db()
