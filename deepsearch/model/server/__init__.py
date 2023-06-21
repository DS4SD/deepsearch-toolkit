from os import getenv

from dotenv import load_dotenv

from deepsearch.model.server.config import Settings

load_dotenv(getenv("DS_MODEL_ENV_FILE"))

settings = Settings(api_key=getenv("DS_MODEL_API_KEY", ""))
