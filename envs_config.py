import os
from dotenv import load_dotenv

load_dotenv()

def obtener_env(variable: str) -> str:
    return os.getenv(variable)