from tkinter import *
import tkinter.messagebox

def numberEnter(nombers):
    global operateur
    operateur = operateur + str(nombers)
    text_input.set(operateur)

def quitter(window):
    quit = tkinter.messagebox.askyesno("calculatrice", "Voulez-vous vraiment quitter la Calculatrice ")
    if quit > 0:
        window.destroy()
        return

def scientific():
    tkinter.messagebox.showinfo("information", "Ce mode de calcule est en cours de construction")

window = Tk()
window.title("calculatrice")
window.resizable(width=False, height=False)
window.geometry("470x460")
text_input = StringVar()
operateur = ""

# ===================Zone d'affichage==================

zoneAffichage = Entry(window, font=("arial", 40, "bold"), width=15, textvariable=text_input, bd=10,
                      bg="lavender", justify="right")
zoneAffichage.grid(columnspan=4)
zoneAffichage.insert(0, "0")

# ====================Barre de Menu====================

"""Menu fichier"""
barre_menu = Menu(window)
menu_fichier = Menu(barre_menu, tearoff=0)
barre_menu.add_cascade(label="fichier", menu=menu_fichier)
menu_fichier.add_command(label="Standard")
menu_fichier.add_command(label="Scientifique", command=scientific)
menu_fichier.add_separator()
menu_fichier.add_command(label="Quitter", command=lambda: quitter(window))

"""Menu edition"""

menu_edition = Menu(barre_menu, tearoff=0)
barre_menu.add_cascade(label="édition", menu=menu_edition)
menu_edition.add_command(label="copier")
menu_edition.add_command(label="couper")
menu_edition.add_command(label="coller")
window.configure(menu=barre_menu)

# ================= Creation des bouttons numerique

"""padnumerique = ("C", "CE", "√", "+/-", "7", "8", "9", "-", "4", "5", "6", "*", "1", "2", "3", "/", "0", ".", "=", 
"+") """
padnumerique = ("7", "8", "9", "4", "5", "6", "1", "2", "3")
i = 0
bouttons = []
for j in range(2, 5):
    for k in range(3):
        bouttons.append(
            Button(window, relief="groove", width=5, bd=6, fg="black", font=("Helvetica", 25, "bold"),
                   text=padnumerique[i]))
        bouttons[i].grid(row=j, column=k)
        bouttons[i]["command"] = lambda x = padnumerique[i]: numberEnter(x)

        i += 1

# ================= Creation des bouttons calcule

btnClean = Button(window, relief="groove", width=5, bd=6, fg="black", font=("Helvetica", 25, "bold"),
                  text="C").grid(row=1, column=0)

btnCleanAll = Button(window, relief="groove", width=5, bd=6, fg="black", font=("Helvetica", 25, "bold"),
                     text="CE").grid(row=1, column=1)

btnSqrt= Button(window, relief="groove", width=5, bd=6, fg="black", font=("Helvetica", 25, "bold"),
                text="√").grid(row=1, column=2)

btnSign= Button(window, relief="groove", width=5, bd=6, fg="black", font=("Helvetica", 25, "bold"),
                text="+/-").grid(row=1, column=3)

btnSqrt= Button(window, relief="groove", width=5, bd=6, fg="black", font=("Helvetica", 25, "bold"),
                text="√").grid(row=1, column=2)

btnSubtract= Button(window, relief="groove", width=5, bd=6, fg="black", font=("Helvetica", 25, "bold"),
                    text="-").grid(row=2, column=3)

btnMulti= Button(window, relief="groove", width=5, bd=6, fg="black", font=("Helvetica", 25, "bold"),
                 text="*").grid(row=3, column=3)

btnDiv= Button(window, relief="groove", width=5, bd=6, fg="black", font=("Helvetica", 25, "bold"),
               text="/").grid(row=4, column=3)

btnAdd= Button(window, relief="groove", width=5, bd=6, fg="black", font=("Helvetica", 25, "bold"),
               text="+").grid(row=5, column=3)

btnZero= Button(window, relief="groove", width=5, bd=6, fg="black", font=("Helvetica", 25, "bold"),
                text="0", command=lambda: numberEnter(0)).grid(row=5, column=0)

btnVirgul= Button(window, relief="groove", width=5, bd=6, fg="black", font=("Helvetica", 25, "bold"),
                  text=".").grid(row=5, column=1)

btnEqual= Button(window, relief="groove", width=5, bd=6, fg="black", font=("Helvetica", 25, "bold"),
                 text="=").grid(row=5, column=2)

btnAdd= Button(window, relief="groove", width=5, bd=6, fg="black", font=("Helvetica", 25, "bold"),
               text="+").grid(row=5, column=3)







window.mainloop()
