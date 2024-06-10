import base64

import requests


class Vision:
    """
    A class to interact with the vision API and generate responses based on an image.

    This class provides methods to send an image along with a textual prompt to a specific vision model
    and obtain a generated response.
    """

    def __init__(self,
                 client):
        """
        Initializes the `Vision` class with a client.

        Parameters:
        - `client`: An instance that contains the base configuration to connect to the API.
        """
        self.client = client

    def generate(self,
                 model: str,
                 messages: str,
                 image_path: str = None,
                 max_tokens: int = 400,
                 priority: int = 1):
        """
        Generates a response based on the provided image.

        Sends a POST request to the API with an image, a prompt, and the desired vision model.

        Parameters:
        - `model`: The vision model to use.
        - `prompt`: The text that will accompany the image to influence the response.
        - `image_path`: The path of the image file (must be a .jpg file).
        - `max_tokens`: The maximum number of tokens in the generated response (optional, default is 400).
        - `priority`: The priority of the request (optional, default is 1).

        Returns:
        - A dictionary containing the API response.

        Exceptions:
        - `ValueError`: If the file is not a .jpg image.
        """

        data = {
            'model': model,
            'messages': messages,
            'max_tokens': max_tokens,
            'priority': priority,
        }
        mime_type = image_path.split(".")[-1]
        if image_path is not None:
            if image_path.startswith("http:/") or image_path.startswith("https:/"):
                data = {
                    'model': model,
                    'messages': messages,
                    'max_tokens': max_tokens,
                    'priority': priority,
                    "image": image_path,
                    "mime_type": mime_type,
                }
            else:
                with open(image_path, "rb") as image_file:
                    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
                data = {
                    'model': model,
                    'messages': messages,
                    'max_tokens': max_tokens,
                    'priority': priority,
                    "image": encoded_image,
                    "mime_type": mime_type,
                }

        response = requests.post(f"{self.client.base_url}/vision", json=data)

        return response.json()["content"]
