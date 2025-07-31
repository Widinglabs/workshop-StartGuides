import os

from anthropic import Anthropic
from dotenv import load_dotenv


class SlideAgent:
    """Simple agent for making Anthropic API calls."""
    
    def __init__(self):
        """Initialize the agent and load environment variables."""
        load_dotenv()
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        
        self.client = Anthropic(api_key=self.api_key)
    
    def run(self):
        """Run the agent with a simple API call."""
        print("= Making API call to Claude...")
        
        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": "Hello! Please respond with a brief, friendly greeting."
                    }
                ]
            )
            
            print("> Claude's response:")
            print(message.content[0].text)
            
        except Exception as e:
            print(f"L Error making API call: {e}")
            raise