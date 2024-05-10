import requests


class Audio:
    """
    A main class that contains submodules to interact with the audio API.

    Submodules:
    - `speech`: For speech synthesis.
    - `transcriptions`: For audio transcription.
    - `translations`: For audio translation.
    """
    def __init__(self, client):
        """
        Initializes the `Audio` class with a specific client.

        Parameters:
        - `client`: An instance that contains the base configuration to connect to the API.
        """
        self.client = client
        self.speech = Speech(self.client)
        self.transcriptions = Transcription(self.client)
        self.translations = Translation(self.client)


class Speech:
    """
    Class to create speech synthesis from text using the audio API.
    """
    def __init__(self, client):
        """
        Initializes the `Speech` class with a client.

        Parameters:
        - `client`: An instance that contains the base configuration to connect to the API.
        """
        self.client = client

    def create(self, model: str,
               prompt: str,
               voice_preset: str = None,
               priority: int = 1):
        """
        Creates speech synthesis from text.

        Parameters:
        - `model`: The speech synthesis model to use.
        - `prompt`: The text to be converted into speech.
        - `voice_preset` (optional): A preset that modifies the characteristics of the generated voice.
        - `priority` (optional): The priority of the speech synthesis task.

        Returns:
        - A `ResponseSpeech` object that contains the synthesized response.
        """
        request_json = {
            'prompt': prompt,
            "model_name": model,
            "voice_preset": voice_preset,
            'priority': priority
        }

        response_data = requests.post(f"{self.client.base_url}/audio/speech", data=request_json)
        return ResponseSpeech(response_data)


class Transcription:
    """
    Class to convert audio files to text via the transcription API.
    """
    def __init__(self, client):
        """
        Initializes the `Transcription` class with a client.

        Parameters:
        - `client`: An instance that contains the base configuration to connect to the API.
        """
        self.client = client

    def create(self, model: str,
               file_path: str,
               language: str = None,
               initial_prompt: str = None,
               priority: int = 1):
        """
        Transcribes an audio file to text.

        Parameters:
        - `model`: The transcription model to use.
        - `file_path`: The path of the audio file to be transcribed.
        - `language` (optional): The language of the audio.
        - `initial_prompt` (optional): An initial prompt that can influence the transcription.
        - `priority`(optional): The priority of the transcription task.

        Returns:
        - A string containing the transcribed text.
        """
        request_json = {
            'model_name': model,
            'language': language,
            'initial_prompt': initial_prompt,
            'priority': priority
        }
        file = open(file_path, "rb")
        audio_file = {"file": file}

        response_data = requests.post(f"{self.client.base_url}/audio/transcriptions", files=audio_file, data=request_json)
        return response_data.json()["text"]


class Translation:
    """
    Class to translate audio files to another language via the translation API.
    """
    def __init__(self, client):
        """
        Initializes the `Translation` class with a client.

        Parameters:
        - `client`: An instance that contains the base configuration to connect to the API.
        """
        self.client = client

    def create(self, model: str,
               file_path: str,
               language: str = None,
               initial_prompt: str = None,
               priority: int = 1):
        """
        Translates an audio file to english language.

        Parameters:
        - `model`: The translation model to use.
        - `file_path`: The path of the audio file to translate.
        - `language` (optional): The target language of the translation.
        - `initial_prompt` (optional): An initial prompt that can influence the translation.
        - `priority` (optional): The priority of the translation task.

        Returns:
        - A string containing the translated text.
        """
        request_json = {
            'model_name': model,
            'language': language,
            'initial_prompt': initial_prompt,
            'priority': priority
        }
        file = open(file_path, "rb")
        audio_file = {"file": file}

        response_data = requests.post(f"{self.client.base_url}/audio/translations", files=audio_file, data=request_json)
        return response_data.json()["text"]


class ResponseSpeech:
    """
    Class to manage the response of speech synthesis.
    """
    def __init__(self, speech):
        """
        Initializes `ResponseSpeech` with a speech synthesis response.

        Parameters:
        - `speech`: The response obtained from the speech synthesis API.
        """
        self.speech = speech

    def stream_to_file(self, path: str):
        """
        Saves the response content to a file.

        Parameters:
        - `path`: The path of the file where the content will be saved.
        """
        with open(path, 'wb') as f:
            f.write(self.speech.content)
