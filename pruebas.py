from openMultIA import OpenMultIA

url = "http://127.0.0.1:5000"

client = OpenMultIA(url)

# Chat
prompt = [
    {"role": "system", "content": "You are a question answering assistant."},
    {"role": "user", "content": "Tell me a number from 1 to 100"},
    {'role': 'assistant', 'content':  'Sure! The answer is... 42!'},
    {"role": "user", "content": "Do you remember what number you said before?"}
]
response = client.chat.completions.create(model="Llama2-7b", messages=prompt, max_tokens=400,
                                          n_gpu_layers=30, n_threads=4, temperature=0.3, top_p=0.92,
                                          top_k=30, stream=False, presence_penalty=0.1, frequency_penalty=0.1,
                                          repeat_penalty=1.2, stop="DONEEE", priority=0)
print(response.choices[0].message)


# Images
# response = client.images.generate(
#     model="sdxl-turbo",
#     prompt="a Norwegian girl putting make up on for her weeding, face must be the principal feature",
# #    n=5,
#     number_steps=4,
#     priority=1
# )
# response.stream_to_file("images.jpg")


# Vision
# messages = [
#     {"role": "user", "content": "describe the image"},
# ]
# http_image = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
# response = client.vision.generate("Llava_4bit", messages=messages, image_path="x.jpg", max_tokens=400, priority=0)
# print(response)


# Transcript
# response = client.audio.transcriptions.create(model="large", file_path="speech.mp3", initial_prompt="fox", language="es", priority=1)
# print(response)

# Translate
# response = client.audio.translations.create(model="large", file_path="speech.mp3", initial_prompt="fox", language="es", priority=1)
# print(response)

# Speech

# speech_file_path = "speech.mp3"
# response = client.audio.speech.create(
#     model="Bark",
#     prompt="EL veloz zorro marrón saltó sobre el perezoso perro",
#     voice_preset="v2/es_speaker_4",
#     priority=1
# )
# response.stream_to_file(speech_file_path)

#List Models
# client.models.list()
