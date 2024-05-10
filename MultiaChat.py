from typing import Union, Optional, List

import requests

from ChatCompletionRequests import ChatCompletionRequestMessage


class Chat:
    """
    A main class that contains submodules to interact with the chat API.

    Submodules:
    - `completions`: For generating chat completions.
    """
    def __init__(self, client):
        """
        Initializes the `Chat` class with a specific client.

        Parameters:
        - `client`: An instance that contains the base configuration to connect to the API.
        """
        self.client = client
        self.completions = Completions(self.client)


class Completions:
    """
    A class to handle the creation of chat completions using the chat API.
    """
    def __init__(self, client):
        """
        Initializes the `Completions` class with a client.

        Parameters:
        - `client`: An instance that contains the base configuration to connect to the API.
        """
        self.client = client

    def create(self, model: str,
               messages: ChatCompletionRequestMessage,
               n_threads: Optional[int] = None,
               n_gpu_layers: int = 0,
               main_gpu: int = 0,
               temperature: int = 0.2,
               max_tokens: int = 512,
               top_p: float = 0.95,
               top_k: int = 40,
               stream: bool = False,
               presence_penalty: float = 0.0,
               frequency_penalty: float = 0.0,
               repeat_penalty: float = 1.1,
               stop: Optional[Union[str, List[str]]] = None,
               priority: int = 1
               ):
        """
        Creates a chat completion request.

        Sends a request to the chat API to generate chat completions based on the specified parameters.

        Parameters:
        - `model`: The model to be used for generating chat completions.
        - `messages`: A list of messages that represent the conversation context.
        - `n_threads` (optional): The number of CPU threads to use.
        - `n_gpu_layers` (optional): The number of layers to process on the GPU.
        - `main_gpu` (optional): The index of the primary GPU to use.
        - `temperature` (optional): The sampling temperature for creative generation.
        - `max_tokens` (optional): The maximum number of tokens to generate.
        - `top_p` (optional): The cumulative probability threshold for sampling.
        - `top_k` (optional): The number of highest-probability tokens to consider during sampling.
        - `stream` (optional): Whether to stream results incrementally.
        - `presence_penalty` (optional): Penalizes new tokens if they've already appeared.
        - `frequency_penalty` (optional): Penalizes tokens that occur frequently.
        - `repeat_penalty` (optional): Penalizes repeating sequences.
        - `stop` (optional): Stop sequences to terminate the generation.
        - `priority` (optional): The priority of the request.

        Returns:
        - A `CompletionsResponse` object containing the generated response, or a streamed response if `stream` is True.
        """
        request_json = {'model_name': model,
                        'n_gpu_layers': n_gpu_layers,
                        'n_threads': n_threads,
                        'main_gpu': main_gpu,
                        'messages': messages,
                        'temperature': temperature,
                        'max_tokens': max_tokens,
                        'top_p': top_p,
                        'top_k': top_k,
                        'stream': stream,
                        'presence_penalty': presence_penalty,
                        'frequency_penalty': frequency_penalty,
                        'repeat_penalty': repeat_penalty,
                        'stop': stop,
                        'priority': priority
                        }

        response_data = requests.post(f"{self.client.base_url}/chat/completions", json=request_json)

        completion = CompletionsResponse(**response_data.json())
        if request_json['stream']:
            return response_data
        return completion


class Choice:
    """
    A class representing a choice within a completion response.
    """
    def __init__(self, index: int, message: dict, finish_reason: str):
        """
        Initializes the `Choice` class with given attributes.

        Parameters:
        - `index`: The index of this choice in the list.
        - `message`: The message content of this choice.
        - `finish_reason`: The reason for finishing this choice.
        """
        self.index = index
        self.message = message
        self.finish_reason = finish_reason


class CompletionsResponse:
    """
    A class representing the response from a chat completions API request.
    """
    def __init__(self, choices: List,

                 created: str,
                 id: str,
                 model: str,
                 object: str,
                 usage: dict,
                 ):
        """
        Initializes the `CompletionsResponse` class.

        Parameters:
        - `choices`: A list of choice objects.
        - `created`: The timestamp of creation.
        - `id`: The ID of the response.
        - `model`: The model used to generate the response.
        - `object`: The object type of the response.
        - `usage`: A dictionary with information about token usage.
        """
        self.usage = usage
        self.object = object
        self.model = model
        self.created = created
        self.id = id
        self.choices = [Choice(**choice) for choice in choices]
