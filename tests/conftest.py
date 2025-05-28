import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'supersecretkey')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:password@localhost:5432/secure_api_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-string')
    RATELIMIT_STORAGE_URI = "memory://"
