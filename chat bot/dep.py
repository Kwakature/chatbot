from ollama import Client

def appelIA(content, modele):
    if content == 'bye':
        client = Client(host='http://localhost:11434')
        response = client.chat(model=modele, messages=[
            {
                'role': 'user',
                'content': 'aurevoir',
            },
        ])
        return response['message']['content']
    else:
        client = Client(host='http://localhost:11434')
        response = client.chat(model=modele, messages=[
            {
                'role': 'user',
                'content': content,
            },
        ])
        return response['message']['content']