from ollama import Client
import dep 
import tkinter as tk

#Creer la fenetre princial 
root = tk.Tk()
# Definition du texte principal 
root.title("Jarvis_V1_ecrit")
# Definition de la taille de la fenaitre 
root.geometry("400x300")

#reation d un label 
label = tk.Label(root, text="Voici Jarvis", font=("Arial", 14))
label.pack()

#ajoue d un bouton 
def on_click():
    Pentrer = entry.get()
    message.config(text=dep.appelIA(Pentrer, dep.ia_default()))


# ajoue d un champs de texte 
entry = tk.Entry(root)
entry.pack(pady=10)

# boutton pour activer les fonction
button = tk.Button(root, text="parler", command=on_click)
button.pack(pady=10)

# affichage reponce 
message = tk.Message(root, text="Reponce", width=350, font=("Arial", 12), bg="lightblue")
message.pack()

# Affichage de la fenetre 
root.mainloop()


'''
while True:
    ia = dep.choix_IA()
    while True:
        entre = input('-->')
        if entre == 'bye':
            print(dep.appelIA(entre, ia))
            break
        else:
            print(dep.appelIA(entre, ia))
'''