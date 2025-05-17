from src.config.config import SESSION_STORAGE_DATABASE_FILENAME
from src.config.config import logger
from src.agent.agent import AgnetAgent

agent = AgnetAgent()

response = agent.agent_response("What is the capital of France?")
print(response)