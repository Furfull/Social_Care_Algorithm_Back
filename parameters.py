from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST")
USERNAME = os.getenv("USERNAME_DB")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
PORT = os.getenv("PORT")
ENDPOINT = os.getenv("ENDPOINT")
KEY = os.getenv("KEY")
FACEBOOKURL = os.getenv("FACEBOOKURL")
EMAIL = os.getenv("EMAIL")
FACEBOOKPASS = os.getenv("FACEBOOKPASS")
ACCOUTSID = os.getenv('TWILIO_ACCOUNT_SID')
AUTHTOKEN = os.getenv('TWILIO_AUTH_TOKEN')