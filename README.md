# OpenMultAI Library

OpenMultIA is a versatile Python library designed to facilitate interaction with the MultAI API, a service that provides the API to perform inference on AI models. OpenMultIA is built to be similar to the OpenAI API, enabling seamless migration from OpenAI to MultAI with minimal adjustments. It provides unified access to audio, chat, images, and vision functionalities.

## Installation

To use OpenMultIA, clone this repository or download it directly, then include it in your Python environment. You can import the library with:

```python
from openMultIA import OpenMultIA
```

## Configuration

Before using the OpenMultIA functionalities, initialize the client with the API's base URL:

```python
url = "http://127.0.0.1:5000"
client = OpenMultIA(url)
```

## Usage

OpenMultIA supports various functionalities provided by the MultAI API, which are demonstrated below:

### Chat

Create chat completions by sending a conversation history and receiving an AI-generated response:

```python
prompt = [
    {"role": "system", "content": "You are a question answering assistant."},
    {"role": "user", "content": "Tell me a number from 1 to 100"},
    {'role': 'assistant', 'content':  'Sure! The answer is... 42!'},
    {"role": "user", "content": "Do you remember what number you said before?"}
]

response = client.chat.completions.create(
    model="Llama2-7b", 
    messages=prompt, 
    max_tokens=400,
    n_gpu_layers=30, 
    n_threads=4, 
    temperature=0.3, 
    top_p=0.92,
    top_k=30, 
    stream=False, 
    presence_penalty=0.1, 
    frequency_penalty=0.1,
    repeat_penalty=1.2, 
    stop="DONEEE", 
    priority=0
)
print(response.choices[0].message["content"])
```

### Images

Generate images based on descriptive prompts:

```python
response = client.images.generate(
    model="sdxl-turbo",
    prompt="Realistic red fox chasing a white bunny",
    n=5,
    number_steps=4
)
response.stream_to_file("images.zip")
```

### Vision

Analyze images to generate descriptive insights:

```python
response = client.vision.generate(
    "Llava_4bit", 
    prompt="What do you see in this image?", 
    image_path="x.jpg", 
    max_tokens=400
)
print(response)
```

### Audio Transcription

Convert audio files into text:

```python
response = client.audio.transcriptions.create(
    model="large", 
    file_path="speech.mp3", 
    initial_prompt="Hola, me llamo Liam. ¿Cómo te llamas tú?", 
    language="es"
)
print(response)
```

### Audio Translation

Translate spoken content from one language to another:

```python
response = client.audio.translations.create(
    model="large", 
    file_path="speech.mp3", 
    initial_prompt="Hola, me llamo Liam. ¿Cómo te llamas tú?", 
    language="es"
)
print(response)
```

### Speech Synthesis

Convert text to speech:

```python
speech_file_path = "speech.mp3"
response = client.audio.speech.create(
    model="Bark",
    prompt="El veloz zorro marrón saltó sobre el perezoso perro",
    voice_preset="v2/es_speaker_4"
)
response.stream_to_file(speech_file_path)
```

## Support

For further information or support, submit an issue in our repository.
