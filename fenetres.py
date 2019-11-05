from tkinter import *
from fenetre.fonctions import quitter
import tkinter.messagebox


fenetre = Tk()
fenetre.title("calculatrice")
fenetre.resizable(width=False, height=False)
fenetre.geometry("600x450")
text_input = StringVar()

# ===================Zone d'affichage==================

zoneAffichage = Entry(fenetre, font=("arial", 40, "bold"), width=20, textvariable=text_input, bd=10,
                      bg="lavender", justify="right")
zoneAffichage.grid(columnspan=4)
zoneAffichage.insert(0, "0")

# ====================Barre de Menu====================


"""Menu fichier"""
barre_menu = Menu(fenetre)
menu_fichier = Menu(barre_menu, tearoff=0)
barre_menu.add_cascade(label="fichier", menu=menu_fichier)
menu_fichier.add_command(label="Standard")
menu_fichier.add_command(label="Scientifique")
menu_fichier.add_separator()
menu_fichier.add_command(label="Quitter", command=lambda:quitter(fenetre))

"""Menu edition"""

menu_edition = Menu(barre_menu, tearoff=0)
barre_menu.add_cascade(label="édition", menu=menu_edition)
menu_edition.add_command(label="copier")
menu_edition.add_command(label="couper")
menu_edition.add_command(label="coller")

fenetre.configure(menu=barre_menu)

# ================= Creation des bouttons numerique
padnumerique = ("C", "CE", "√", "+/-", "7", "8", "9", "-", "4", "5", "6", "*", "1", "2", "3", "/", "0", ".", "=", "+")
i = 0
bouttons = []
for j in range(1, 6):
    for k in range(4):
        bouttons.append(
            Button(fenetre, relief="groove", width=6, bd=5, fg="black", font=("Helvetica", 25, "bold"),
                   text=padnumerique[i]))
        bouttons[i].grid(row=j, column=k)
        i += 1


fenetre.mainloop()
