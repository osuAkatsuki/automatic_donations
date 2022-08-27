from os import environ

from dotenv import load_dotenv

load_dotenv()

PAYPAL_WEBHOOK_ID = environ["PAYPAL_WEBHOOK_ID"]

DB_HOST = environ["DB_HOST"]
DB_PORT = environ["DB_PORT"]
DB_USER = environ["DB_USER"]
DB_PASS = environ["DB_PASS"]
DB_NAME = environ["DB_NAME"]
DB_DSN = f"mysql+asyncmy://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
