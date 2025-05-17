from agno.agent import Agent
from agno.models.google import Gemini
# from agno.models.groq import Groq
from src.config.config import (
    AGENT_ID,
    AGENT_NAME,
    GEMINI_API_KEY,
    logger
)
class AgnetAgent:
    def __init__(self, agent_id: str=AGENT_ID, agent_name: str=AGENT_NAME):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.agent = Agent(
            agent_id=self.agent_id,
            name=self.agent_name,
            model=Gemini(id ="gemini-1.5-flash", api_key=GEMINI_API_KEY),
            markdown=True,
            stream_intermediate_steps=False,
        )
        
    def agent_response(self, user_input: str):
        response = self.agent.run(user_input)
        return response.content
