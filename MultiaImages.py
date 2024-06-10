import requests


class Images:
    """
    A class to interact with the image generation API.

    This class provides methods to generate images based on prompts using a specific model.
    """
    def __init__(self, client):
        """
        Initializes the `Images` class with a specific client.

        Parameters:
        - `client`: An instance that contains the base configuration to connect to the API.
        """
        self.client = client

    def generate(self,
                 model: str,
                 prompt: str,
                 n: int = 1,
                 number_steps: int = 4,
                 priority: int = 1):
        """
        Generates images based on the given prompt.

        Sends a POST request to the API to generate images with the specified model and prompt.

        Parameters:
        - `model`: The name of the model to be used for image generation.
        - `prompt`: A description to guide the image generation.
        - `n`: The number of images to generate (default is 1).
        - `number_steps`: The number of steps in the image generation process (default is 4).
        - `priority`: The priority of the image generation request (default is 1).

        Returns:
        - A `ResponseImage` object containing the generated images.
        """
        request_json = {
            'prompt': prompt,
            'model': model,
            'n': n,
            'number_steps': number_steps,
            'priority': priority
        }

        images = requests.post(f"{self.client.base_url}/images/generations", json=request_json)
        return ResponseImage(images, n)


class ResponseImage:
    """
    A class to manage the response of image generation requests.
    """
    def __init__(self, images, n):
        """
        Initializes the `ResponseImage` class.

        Parameters:
        - `images`: The raw image data returned by the API.
        - `n`: The number of images generated.
        """
        self.images = images
        self.n = n

    def stream_to_file(self,
                       path: str):
        """
        Saves the generated images to a file.

        Parameters:
        - `path`: The path of the file where the images will be saved.

        Raises:
        - `ValueError`: If the file extension does not match the expected format based on the number of images.
        """
        if self.n > 1:
            if not path.endswith("zip"):
                raise ValueError('There are multiple images, so they must be stores in .zip file, change filename extension for .zip')
            with open(path, 'wb') as f:
                f.write(self.images.content)
        else:
            if not path.endswith('jpg'):
                raise ValueError('Output files are jpg, please change file extension for .jpg for proper output')
            with open(path, 'wb') as f:
                f.write(self.images.content)
