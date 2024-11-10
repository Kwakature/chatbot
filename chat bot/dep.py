from ollama import Client

def appelIA(content, modele):
        client = Client(host='http://localhost:11434')
        response = client.chat(model=modele, messages=[
            {
                'role': 'user',
                'content': content,
            },
        ])
        return response['message']['content']
    
def choix_IA():
    """
    fonction a utiliser pour une interface text
    """
    print("1 : llama3.1:latest")
    print("2 : gemma2:27b")
    numero = int(input('choisi l IA a utiliser : '))
    if numero == 1:
        nomIA = 'llama3.1:latest'
    if numero == 2:
        nomIA = 'gemma2:27b'
    return nomIA