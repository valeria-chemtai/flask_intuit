import os


DEBUG = False
ENVIRONMENT = os.getenv('ENVIRONMENT', 'Sandbox')
SECRET_KEY = os.getenv('SECRET_KEY', 'abcdefgh')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI', 'http://lvh.me:5000/callback')
API_MINORVERSION = os.getenv('API_MINORVERSION')
