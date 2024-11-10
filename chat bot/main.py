from ollama import Client
import dep 

while True:
    ia = dep.choix_IA()
    while True:
        entre = input('-->')
        if entre == 'bye':
            print(dep.appelIA(entre, ia))
            break
        else:
            print(dep.appelIA(entre, ia))