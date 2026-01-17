from ollama import chat
from ollama import ChatResponse
from spt import decodificar

def usar_ia():
    texto = decodificar()

    response: ChatResponse = chat(model='llama3.1:8b', messages=[
    {
        'role': 'user',
        'content': f'{texto}',
    },
    ])
    return response.message.content


