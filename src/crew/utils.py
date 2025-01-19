"""
Utility functions for the Happy Guy application.
This module provides helper functions for HTML template manipulation.
"""

from typing import Optional, Dict, Any

def update_html_template(
    file_path: str,
    replacements: Dict[str, Any],
    output_path: Optional[str] = './outputs/output.html'
) -> Optional[str]:
    """
    Update an HTML template by replacing placeholders with actual values.
    
    Args:
        file_path (str): Path to the HTML template file
        replacements (Dict[str, Any]): Dictionary of placeholder-value pairs for replacement
        output_path (Optional[str]): Path to save the updated HTML file. 
                                   If None, returns the updated content instead.
    
    Returns:
        Optional[str]: Updated HTML content if output_path is None, otherwise None
        
    Raises:
        IOError: If there are issues reading from or writing to files
    """
    try:
        # Read the HTML template file
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Replace all placeholders with their corresponding values
        for placeholder, value in replacements.items():
            html_content = html_content.replace(placeholder, str(value))

        # Either save to file or return the content
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(html_content)
            print(f"Updated HTML saved to {output_path}")
            return None
        return html_content
        
    except IOError as e:
        print(f"Error processing HTML template: {str(e)}")
        raise