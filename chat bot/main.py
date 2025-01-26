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
    selectionner = ia_select.get()
    message.config(text=dep.appelIA(Pentrer, selectionner))

#boutton radio de selection d Ia a utiliser 
ia_select = tk.StringVar()
ia_select.set("llama3.1:latest")
selectionner = ia_select.get()

#affichage bouton radio
r1 = tk.Radiobutton(root, text="llama3.1", variable=ia_select, value="llama3.1:latest")
r1.pack()

r2 = tk.Radiobutton(root, text="gemma2", variable=ia_select, value="gemma2:27b")
r2.pack()

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