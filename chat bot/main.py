from ollama import Client
import dep 

while True:
    print("1 : llama3.1:latest")
    print("2 : gemma2:27b")
    model = int(input('choix IA'))
    if model == 1 :
        ia = 'llama3.1:latest'
    if model == 2 :
        ia = 'gemma2:27b'
    if model > 2:
        ia = 'stop'
        print('erreur retry')
    while True:
        entre = input('-->')
        if entre == 'bye':
            print(dep.appelIA(entre, ia))
            break
        else:
            print(dep.appelIA(entre, ia))