import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': 'A photograph of the inside of a subway train. There are raccoons sitting on the seats. One of them is reading a newspaper. The window shows the city in the background.',
    },
    headers={'api-key': '98df9e5d-ec96-4f94-94a2-d8be54418791'}
)
print(r.json())