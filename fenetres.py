from tkinter import *


def btnclik(nombers):
        global operateur
        operateur = operateur + str(nombers)
        text_input.set(operateur)


def btn_clik_clean():
        global operateur
        operateur = ""
        text_input.set("")


def btn_clik_eq():
        global operateur
        result = str(eval(operateur))
        text_input.set(result)
        operateur = result


def creation_button_num(txt, rowbtn, columnbtn):
    Button(fenetre, padx=20, pady=15, bd=5, fg="black", font=("arial", 18, "bold"), text=txt,
           command=lambda: btnclik(txt)).grid(row=rowbtn, column=columnbtn)


def creation_button_clean(txt, rowbtn, columnbtn):
    Button(fenetre, padx=20, pady=15, bd=5, fg="black", font=("arial", 18, "bold"), text=txt,
           command=lambda: btn_clik_clean()).grid(row=rowbtn, column=columnbtn)


def creation_button_eq(txt, rowbtn, columnbtn):
    Button(fenetre, padx=20, pady=15, bd=5, fg="black", font=("arial", 18, "bold"), text=txt,
           command=lambda: btn_clik_eq()).grid(row=rowbtn, column=columnbtn)


fenetre = Tk()
fenetre.title("calculatrice")
operateur = ""
text_input = StringVar()

zoneAffichage = Entry(fenetre, font=("arial", 20, "bold"), textvariable=text_input, bd=10, insertwidth=4,
                      bg="lavender", justify="right").grid(columnspan=4)

creation_button_num(0, 4, 1)
creation_button_num(1, 3, 0)
creation_button_num(2, 3, 1)
creation_button_num(3, 3, 2)
creation_button_num(4, 2, 0)
creation_button_num(5, 2, 1)
creation_button_num(6, 2, 2)
creation_button_num(7, 1, 0)
creation_button_num(8, 1, 1)
creation_button_num(9, 1, 2)
creation_button_num("+", 4, 3)
creation_button_num("-", 3, 3)
creation_button_num("*", 2, 3)
creation_button_num("/", 1, 3)
creation_button_clean("C",4,0)
creation_button_eq("=",4,2)

fenetre.mainloop()
