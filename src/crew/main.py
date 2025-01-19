"""
Main module for the Happy Guy application.
This module handles the execution of the crew workflow and manages the output generation.
"""

from .utils import update_html_template
from crew.crew import HappyCrew
from crew import mapping
import pickle 

def fetch_content(inputs: dict) -> None:
    """
    Execute the crew workflow and save the output to a pickle file.
    
    Args:
        inputs (dict): Dictionary containing input parameters:
            - person (str): Name of the person
            - event (str): Type of event (birthday, work anniversary, etc.)
            - event_date (str): Date of the event in DD-MM-YYYY format
    """
    # Run the crew workflow
    d = HappyCrew().crew().kickoff(inputs=inputs).to_dict()

    # Save output to a pickle file for persistence
    with open("./outputs/output.pkl", "wb") as f:
        pickle.dump(d, f)


def run() -> None:
    """
    Main function to execute the workflow with sample inputs.
    Processes the content and updates the appropriate HTML template.
    """
    # Sample inputs - can be modified as needed
    inputs = {
        'person': 'Abhinava Bharat',
        'event': "Birthday",
        'event_date': '20-01-1997',
        'company': 'AB InBev/Anheuser-Busch InBev GCC',
        'words':'200',
    }

    # Generate and save content
    fetch_content(inputs)

    # Load the generated content
    with open("./outputs/output.pkl", "rb") as file:
        d = pickle.load(file)

    # Update the appropriate HTML template based on event type
    for event, path in mapping.items():
        if d['event_type'].lower() == event:
            update_html_template(file_path=path, replacements=d)