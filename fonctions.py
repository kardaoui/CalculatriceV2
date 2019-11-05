import tkinter
import fenetre

import tkinter.messagebox




# ==================fonction Quitter du menu
def quitter(fenetre):
    quitter = tkinter.messagebox.askyesno("calculatrice", "Voulez-vous vraiment quitter la Calculatrice ")
    if quitter > 0:
        fenetre.destroy()
        return






def btnclik(txt):
    global operateur
    operateur = operateur + str(txt)
    #text_input.set(operateur)


def btn_clik_clean():
    global operateur
    operateur = ""
    #text_input.set("")


def btn_clik_eq():
    global operateur
    try:
        result = str(eval(operateur))
        #text_input.set(result)
        operateur = result
    except:
        #text_input.set("ERROR")
        operateur = ""



#def creation_button_clean(txt, rowbtn, columnbtn):
#    Button(fenetre, width=5, pady=15, bd=5, fg="black", font=("arial", 18, "bold"), text=txt,
#           command=lambda: btn_clik_clean()).grid(row=rowbtn, column=columnbtn)
#
#
#def creation_button_eq(txt, rowbtn, columnbtn):
#    Button(fenetre, width=5, pady=15, bd=5, fg="black", font=("arial", 18, "bold"), text=txt,
#           command=lambda: btn_clik_eq()).grid(row=rowbtn, column=columnbtn)
