import os
from pathlib import Path
import logging
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROK_API_KEY = os.getenv("GROK_API_KEY")
SESSION_STORAGE_TABLE_NAME = "AGNET_SESSION"
SESSION_STORAGE_DATABASE_FILENAME = "AGNET_SESSION.db"
USER_MEMORIES_TABLE_NAME = "AGNET_USER_MEMORIES"
USER_MEMORIES_DATABASE_FILENAME = "AGNET_MEMORY.db"
AGENT_ID = "AGNET-800"
AGENT_NAME = "AGNET"
SESSION_TIMEOUT = 5*60 # 5 minutes
MODEL_LIST = [
    "gemini",
    "groq"
]

# LOGGING CONFIG

logging.getLogger("httpcore").setLevel(logging.ERROR)
logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("google_genai").setLevel(logging.ERROR)
logging.getLogger("AGNET").setLevel(logging.INFO) 
LOGGING_PATH = Path("src/logs")

# Ensure the logging directory exists
LOGGING_PATH.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s %(filename)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(LOGGING_PATH, "agent.log")),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("AGNET")
