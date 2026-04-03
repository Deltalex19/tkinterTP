import tkinter as tk
from idlelib.outwin import file_line_pats
from tkinter.constants import BOTTOM
from tkinter import messagebox
def renvoyer_age():
    age = entryage.get()
    taille = entrytaille.get()

if age >= 15:
  labelallow.config(text="Manège autorisé", fg="blue")

fenetre = tk.Tk()
fenetre.geometry("450x300")
fenetre.title("TP Manège Parc d'Attraction - BTS CIEL")
labeltitre = tk.Label(fenetre, text="Manège du parc - Force1/Force2", font=("Arial", 18), bg='mintcream', fg='navy')
labeltitre.pack(fill='both',padx=0,pady=0,side='top')
labeldesc = tk.Label(fenetre, text="Entrez votre âge et votre taille pour savoir à quelle force vous pouvez faire le manège.", wraplength=350, font=("Arial", 12))
labeldesc.pack(fill='both',padx=0,pady=0)
labelage = tk.Label(fenetre, text="Entrez votre âge :", wraplength=250, font=("Arial", 10))
labelage.pack(fill='both',padx=0,pady=3)
entryage =tk.Entry(fenetre)
entryage.pack(fill='both',padx=130,pady=3)
labeltaille = tk.Label(fenetre, text="Entrez votre taille (en m,exemple: 1.73) :", wraplength=300, font=("Arial", 10))
labeltaille.pack(fill='both',padx=0,pady=3)
entrytaille =tk.Entry(fenetre)
entrytaille.pack(fill='both',padx=130,pady=3)
buttonenv = tk.Button(fenetre, text="Envoyer", bg='white', command=renvoyer_age)
buttonenv.pack(fill='both',padx=185,pady=9)
labelallow =tk.Label(fenetre, text="")
labelallow.pack(fill='both',padx=0,pady=0,side='bottom')
fenetre.mainloop()