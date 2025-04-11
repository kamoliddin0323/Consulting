from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("API_TOKEN")  

DB_CONFIG = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),  
    "host": os.getenv("DB_HOST"),  
    "port": os.getenv("DB_PORT")  
}
