"""
Initialization module for the Happy Guy application.
Handles environment setup and defines core data structures.
"""

import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# Load environment variables from .env file
load_dotenv(dotenv_path=r'/Users/abhinavgavireddi/Desktop/projects/engagement_project/happy_guy/.env')

# Set required API keys from environment variables
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
os.environ['SERPLY_API_KEY'] = os.getenv('SERPER_API_KEY')

# Mapping of event types to their corresponding HTML templates
mapping = {
    'birthday': './html_templates/birthday.html',
    'farewell': './html_templates/farewell.html',
    'work anniversary': './html_templates/work_anniversary.html'
}

class OutputFormat(BaseModel):
    """
    Pydantic model defining the structure of the message output.
    
    Attributes:
        name (str): Name of the person to address in the message
        event_type (str): Type of event (birthday, farewell, work anniversary)
        content (str): The main message content
    """
    name: str = Field(
        ...,
        description="Appropriate name of person to address in email"
    )
    event_type: str = Field(
        ...,
        description="Birthday, Farewell, Work Anniversary"
    )
    content: str = Field(
        ...,
        description="Email content"
    )