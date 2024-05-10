from MultiaAudio import Audio
from MultiaChat import Chat
from MultiaImages import Images
from MultiaVision import Vision
from Models import Models

class OpenMultIA:
    """
    A client class to interact with various MultIA services including chat, audio, images, and vision.

    This class consolidates all the different services provided by the MultIA API, enabling access through
    a single interface.
    """
    def __init__(self, base_url):
        """
        Initializes the `OpenMultIA` client with the provided base URL.

        The instance variables represent the submodules, making them available through this client.

        Parameters:
        - `base_url`: The base URL of the MultIA API.
        """
        self.base_url = base_url
        self.chat = Chat(self)
        self.audio = Audio(self)
        self.images = Images(self)
        self.vision = Vision(self)
        self.models = Models(self)




