from dotenv import load_dotenv, find_dotenv
import os
_ = load_dotenv(find_dotenv())

class Settings:
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    REDSHIFT_HOST = os.getenv('REDSHIFT_HOST')
    REDSHIFT_DATABASE = os.getenv('REDSHIFT_DATABASE')
    REDSHIFT_USER = os.getenv('REDSHIFT_USER')
    REDSHIFT_PASSWORD = os.getenv('REDSHIFT_PASSWORD')
    REDSHIFT_PORT = os.getenv('REDSHIFT_PORT')
    REGION =  os.getenv('REGION')