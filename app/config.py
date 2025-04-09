import os
database = os.getenv("database")

class Config:
    SQLALCHEMY_DATABASE_URI = database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
