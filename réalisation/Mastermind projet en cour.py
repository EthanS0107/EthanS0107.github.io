# Voici un Mastermind créé par Ethan Serville le26/02/2024

#Imports
from tkinter import *
import tkinter.font as font

class Buttons:
    def __init__(self, fen1, grille):
        self.buttons = []
        self.boutondejeu = []
        self.Tbcolors = ["red", "yellow", "green", "blue", "purple", "orange"]
        self.Grille = grille

        # Creation des boutons colores
        for ind in range(6):
            self.buttons.append(Button(fen1, width=5, bg=self.Tbcolors[ind], command=lambda x=ind: self.Tbcolor_button(x)))
            self.buttons[ind].place(x=400 + 50 * ind, y=480)

        for ind1 in range(5):
            self.boutondejeu.append(Button(fen1, width=4, height=2, bg=self.Tbcolors[ind1], command=lambda x=ind1: self.fct_button(x)))

    def Tbcolor_button(self, nb):
        global couleur
        couleur = self.Tbcolors[nb]
        for ind in range(5):
            self.boutondejeu[ind].config(bg=self.Tbcolors[nb])
            self.boutondejeu[ind].place(x=25 + 40 * ind, y=520)

    def fct_button(self, nb):
        self.Grille.create_oval(10 + 40 * nb, 370, 10 + 40 * nb + 30, 370 + 30, fill=couleur)
        for ind in range(5):
            self.boutondejeu[ind].place_forget()


class MastermindInterface:
    def __init__(self):
        
        # Definition de la fenêtre
        self.fen1 = Tk()
        self.fen1.title("Jeu Mastermind ")
        self.fen1.geometry("750x600")
        
        # Creation de la grille
        self.Grille = Canvas(self.fen1, width=510, height=600)
        self.Grille.place(x=20, y=150)

        # Creation des lignes
        for i in range(9):
            self.Grille.create_line(5 + i * 40, 8, 5 + i * 40, 408, width=2)

        # Creation des colonnes
        for i in range(11):
            self.Grille.create_line(5, 8 + i * 40, 205, 8 + i * 40, width=2)
            self.Grille.create_line(245, 8 + i * 40, 325, 8 + i * 40, width=2)

        self.buttons = Buttons(self.fen1, self.Grille)

        # Creation des boutons Valide, Annule, Quitter
        Valide = Button(self.fen1, text="Validé", width=7, fg="blue", bg="grey")
        Annule = Button(self.fen1, text="Annulé", width=7, fg="white", bg="grey")
        Quitter = Button(self.fen1, text="Quitter", width=7, fg="red", bg="grey", command=self.fen1.destroy)

        Valide.place(x=400, y=530)
        Annule.place(x=515, y=530)
        Quitter.place(x=635, y=530)

        # police d'ecriture et taille
        f = font.Font(family='Arial', size=14)

        # Consigne
        L1 = Label(self.fen1, text="Déterminer les pions de couleurs choisis aléatoirement", fg="black")
        L2 = Label(self.fen1, text="Chaque couleur peut être répétée plusieurs fois", fg="black")
        L3 = Label(self.fen1, text="Cliquer sur le bouton correspondant à la couleur choisie", fg="black")
        L4 = Label(self.fen1, text="Puis, cliquer sur la case souhaitée pour placer votre pion", fg="black")
        L5 = Label(self.fen1, text="Lorsque la ligne est complète VALIDER pour passer à l'essai suivant", fg="blue")
        L6 = Label(self.fen1, text="Une fois la ligne validée :", fg="black")
        L7 = Label(self.fen1, text="chaque point noir correspond à un pion", fg="black")
        L8 = Label(self.fen1, text="pion de bonne couleur et bien placé", fg="black")
        L9 = Label(self.fen1, text="chaque point blanc correspond à un", fg="black")
        L10 = Label(self.fen1, text="pion de bonne couleur mais mal placé", fg="black")

        # Appliquer la police et la taille
        L1['font'] = f
        L2['font'] = f
        L3['font'] = f
        L4['font'] = f
        L5['font'] = f
        L6['font'] = f
        L7['font'] = f
        L8['font'] = f
        L9['font'] = f
        L10['font'] = f

        # place les consignes
        L1.place(x=20, y=10)
        L2.place(x=20, y=35)
        L3.place(x=20, y=60)
        L4.place(x=20, y=85)
        L5.place(x=20, y=110)
        L6.place(x=450, y=160)
        L7.place(x=400, y=185)
        L8.place(x=400, y=210)
        L9.place(x=400, y=245)
        L10.place(x=400, y=270)

    def run(self):
        self.fen1.mainloop()


if __name__ == "__main__":
    mastermind_interface = MastermindInterface()
    mastermind_interface.run()