from tkinter import *
import tkinter.font as font
from random import choice

class Pacman:
    def __init__(self, canvas, x, y, murs, score_lab, f, interface):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.murs = murs
        self.pacman_score = 0
        self.bouche = 1
        self.pacman = canvas.create_arc(x, y, x + 30, y + 30, fill="yellow", start=15, extent=330)
        self.score_lab = score_lab
        self.f = f
        self.interface = interface
        self.position = (x, y)

    def move(self, direction):
        global colonne, ligne
        colonne = self.x // 30
        ligne = self.y // 30
        self.canvas.delete(self.pacman)
        self.eat_orange_candy(direction)
        if direction == "bas" and self.y < 510 and self.murs[ligne + 1][colonne] != 1:
            self.y += 30
        elif direction == "haut" and self.y > 0 and self.murs[ligne - 1][colonne] != 1:
            self.y -= 30
        elif direction == "gauche" and self.x > 0 and self.murs[ligne][colonne - 1] != 1:
            self.x -= 30
            if self.y == 240 and self.x == 0:
                self.x = 480
                self.y = 240
        elif direction == "droite" and self.x < 480 and self.murs[ligne][colonne + 1] != 1:
            self.x += 30
            if self.y == 240 and self.x >= 480:
                self.x = 0
                self.y = 240
        self.update_pacman(direction)
        self.position = (self.x, self.y)
        

    def update_pacman(self, direction):
        if direction == "droite" :
            self.pacman = self.canvas.create_arc(self.x, self.y, self.x + 30, self.y + 30, fill="yellow", start=15, extent=330)
        
        if direction == "gauche" :
            self.pacman = self.canvas.create_arc(self.x, self.y, self.x + 30, self.y + 30, fill="yellow", start=195, extent=330)
            
        if direction == "bas" :
            self.pacman = self.canvas.create_arc(self.x, self.y, self.x + 30, self.y + 30, fill="yellow", start=285, extent=330)
        
        if direction == "haut" :
            self.pacman = self.canvas.create_arc(self.x, self.y, self.x + 30, self.y + 30, fill="yellow", start=105, extent=330)
            
    def eat_orange_candy(self, direction) :
        if direction == "droite" :
            if self.murs[ligne][colonne + 1] == 2 :
                self.murs[ligne][colonne + 1]=0
                self.canvas.create_oval(30*(colonne+1) +12, 30*ligne+12, 30*(colonne+1)+18, 30*ligne+18, fill="#000000")
                self.pacman_score = self.pacman_score + 1
                self.score_lab.config(text=self.pacman_score)
        if direction == "gauche" :
            if self.murs[ligne][colonne - 1] == 2 :
                self.murs[ligne][colonne - 1]=0
                self.canvas.create_oval(30*(colonne-1) +12, 30*ligne+12, 30*(colonne-1)+18, 30*ligne+18, fill="#000000")
                self.pacman_score = self.pacman_score + 1
                self.score_lab.config(text=self.pacman_score)
        if direction == "bas" :
            if self.murs[ligne + 1][colonne] == 2 :
                self.murs[ligne + 1][colonne]=0
                self.canvas.create_oval(30*colonne +12, 30*(ligne+1)+12, 30*colonne+18, 30*(ligne+1)+18, fill="#000000")
                self.pacman_score = self.pacman_score + 1
                self.score_lab.config(text=self.pacman_score)
        if direction == "haut" :
            if self.murs[ligne - 1][colonne] == 2 :
                self.murs[ligne - 1][colonne]=0
                self.canvas.create_oval(30*colonne +12, 30*(ligne-1)+12, 30*colonne+18, 30*(ligne-1)+18, fill="#000000")
                self.pacman_score = self.pacman_score + 1
                self.score_lab.config(text=self.pacman_score)
                
        if self.pacman_score == 125 :
            self.interface.end_game("win")

class FantomeBleu() :
    def __init__(self, canvas, x, y, pacman, interface) :
        self.canvas = canvas
        self.x = x
        self.y = y
        self.pacman = pacman
        self.fantome_bleu = canvas.create_oval(x, y, x + 30, y + 30, fill="blue")
        self.interface = interface
        self.move_count = 0
        self.start_sequence = [(x - 30, y), (x - 30, y - 30), (x - 30, y - 60)]
        
    def move(self):
        if self.move_count < len(self.start_sequence):
            self.move_to_start_zone()
        else:
            direction = self.random_move()
            while not self.direction_sans_mur(direction):
                direction = self.random_move()

            next_position = self.next_position(direction)

            if next_position:
                self.x, self.y = next_position

                self.canvas.delete(self.fantome_bleu)
                self.fantome_bleu = self.canvas.create_oval(self.x, self.y, self.x + 30, self.y + 30, fill="blue")

            if (self.x, self.y) == (self.pacman.x, self.pacman.y):
                self.interface.game_over()

        self.move_count += 1

    def direction_sans_mur(self, direction):
        next_position = self.next_position(direction)
        return next_position is not None

    def move_to_start_zone(self):
        next_position = self.start_sequence[self.move_count]
        self.x, self.y = next_position

        self.canvas.delete(self.fantome_bleu)
        self.fantome_bleu = self.canvas.create_oval(self.x, self.y, self.x + 30, self.y + 30, fill="blue")
          
        
    def random_move(self):
        possible_moves = ["droite", "gauche", "bas", "haut"]
        return choice(possible_moves)
    
    def next_position(self, direction):
        next_x, next_y = self.x, self.y

        if direction == "droite" and self.x < 480 and self.pacman.murs[self.y // 30][self.x // 30 + 1] != 1:
            next_x += 30
        elif direction == "gauche" and self.x > 0 and self.pacman.murs[self.y // 30][self.x // 30 - 1] != 1:
            next_x -= 30
        elif direction == "bas" and self.y < 480 and self.pacman.murs[self.y // 30 + 1][self.x // 30] != 1:
            next_y += 30
        elif direction == "haut" and self.y > 0 and self.pacman.murs[self.y // 30 - 1][self.x // 30] != 1:
            next_y -= 30

        return next_x, next_y
    
class FantomeJaune() :
    def __init__(self, canvas, x, y, pacman, interface) :
        self.canvas = canvas
        self.x = x
        self.y = y
        self.pacman = pacman
        self.fantome_jaune = canvas.create_oval(x, y, x + 30, y + 30, fill="yellow")
        self.interface =interface
        
    def move(self):
        start = (self.x // 30, self.y // 30)
        end = (self.pacman.x // 30, self.pacman.y // 30)

        stock_chemain = self.recherche_chemain(start, end)

        if stock_chemain:
            if len(stock_chemain) >= 1:
                next_position = stock_chemain[1]
                self.x, self.y = next_position[0] * 30, next_position[1] * 30
            else:
                self.x += 30
                
            self.canvas.delete(self.fantome_jaune)
            self.fantome_jaune = self.canvas.create_oval(self.x, self.y, self.x + 30, self.y + 30, fill="yellow")

        if (self.x, self.y) == (self.pacman.x, self.pacman.y):
            self.interface.game_over()
    
    def recherche_chemain(self, start, end):
        visited = set()
        queue = [(start, [start])]

        while queue:
            position_actuel, stock_chemain = queue.pop(0)
            if position_actuel in visited:
                continue
            visited.add(position_actuel)

            if position_actuel == end or (position_actuel[0] == end[0] and abs(position_actuel[1] - end[1]) <= 2):
                return stock_chemain

            for voisin in self.position_voisine(position_actuel):
                queue.append((voisin, stock_chemain + [voisin]))
        return []

    def position_voisine(self, pos):
        x, y = pos
        candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        valid_position_voisine = [voisin for voisin in candidates if 0 <= voisin[0] < len(self.pacman.murs[0]) and 0 <= voisin[1] < len(self.pacman.murs) and self.pacman.murs[voisin[1]][voisin[0]] != 1]
        return valid_position_voisine
    
class FantomeRouge:
    def __init__(self, canvas, x, y, pacman,interface):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.pacman = pacman
        self.fantom_rouge = canvas.create_oval(x, y, x + 30, y + 30, fill="red")
        self.interface =interface

    def move(self):
        start = (self.x // 30, self.y // 30)
        end = (self.pacman.x // 30, self.pacman.y // 30)

        stock_chemain = self.recherche_chemain(start, end)

        if stock_chemain :
            next_position = stock_chemain[1]
            self.x, self.y = next_position[0] * 30, next_position[1] * 30

            self.canvas.delete(self.fantom_rouge)
            self.fantom_rouge = self.canvas.create_oval(self.x, self.y, self.x + 30, self.y + 30, fill="red")
        
        if (self.x, self.y) == (self.pacman.x, self.pacman.y):
            self.interface.game_over()

    def recherche_chemain(self, start, end):
        visited = set()
        queue = [(start, [start])]

        while queue:
            position_actuel, stock_chemain = queue.pop(0)
            if position_actuel in visited:
                continue # permet d'éviter de rechercherle même chemain et donc passe à la suite de la boucle, cela évite de devoir rajouté un grand nombre de condition
            visited.add(position_actuel)

            if position_actuel == end:
                return stock_chemain

            for voisin in self.position_voisine(position_actuel):
                queue.append((voisin, stock_chemain + [voisin]))
        return []

    def position_voisine(self, pos):
        x, y = pos
        candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        valid_position_voisine = [voisin for voisin in candidates if 0 <= voisin[0] < len(self.pacman.murs[0]) and 0 <= voisin[1] < len(self.pacman.murs) and self.pacman.murs[voisin[1]][voisin[0]] != 1]
        return valid_position_voisine
    
class Interface_game:
    def __init__(self):
        
        self.end_game_message = ""
         
        self.murs = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1],
                    [1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1],
                    [1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1],
                    [1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1],
                    [0, 0, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 0, 0],
                    [0, 0, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 0, 0],
                    [1, 1, 1, 2, 2, 2, 1, 1, 0, 1, 1, 2, 2, 2, 1, 1, 1],
                    [3, 2, 2, 2, 1, 2, 1, 0, 0, 0, 1, 2, 1, 2, 2, 2, 3],
                    [1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1],
                    [0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0],
                    [1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1],
                    [1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1],
                    [1, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1],
                    [1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 1],
                    [1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.root = Tk()
        self.root.title("Pacman Game")
        self.root.geometry("710x515")

        self.canvas = Canvas(self.root, width=510,height=510, bg="black")
        self.canvas.place(x=0, y=0)
        
        self.f_70 = font.Font(family='Arial', size=70)
        self.f_100 = font.Font(family='Arial', size=100)
        self.score = Label(self.root, text="0", fg="red")
        self.score.place(x=545, y=200)
        self.score['font'] = self.f_70

        self.create_maze()
        self.pacman = Pacman(self.canvas, 30, 30, self.murs, self.score, self.f_70, self)
        self.fantome_rouge = FantomeRouge(self.canvas, 210, 240, self.pacman, self)
        self.fantome_jaune = FantomeJaune(self.canvas, 240, 240, self.pacman, self)
        self.fantome_bleu = FantomeBleu(self.canvas, 270, 240, self.pacman, self)

        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        
        self.root.mainloop()
        
    def create_maze(self):
        for y in range(len(self.murs)):
            for x in range(len(self.murs[y])):
                if self.murs[y][x] == 1:
                    self.canvas.create_rectangle(30*x,30*y,30*x+30,30*y+30, fill="blue", tags="wall")
                elif self.murs[y][x] == 2:
                    self.canvas.create_oval(30*x +12, 30*y+12, 30*x+18, 30*y+18, fill="orange", tags="orange_candy")

    def end_game(self, result):
        if result == "win":
            self.end_game_message = "Félicitations, vous avez gagné !"
        else:
            self.end_game_message = "Dommage, vous avez perdu. Essayez encore !"

        self.root.destroy()

        end_window = Tk()
        end_window.title("Fin de la partie")
        end_window.geometry("710x515")
        end_window.configure(bg="black")

        # Ajout d'un Frame pour centrer le contenu
        center = Frame(end_window, bg="black")
        center.pack(expand=True)

        end_game_label = Label(center, text=self.end_game_message, font=self.f_100, fg="green" if result == "win" else "red", bg="black")
        end_game_label.pack(pady=(10, 0))

        quit_button = Button(center, text="Quitter", command=end_window.quit)
        quit_button.pack(pady=(0, 10), padx=5)

        end_window.mainloop()


    def game_over(self):
         self.end_game("lose")

    def move_up(self, event):
        self.pacman.move("haut")
        if not self.check_collision():
            self.fantome_rouge.move()
            self.fantome_jaune.move()
            self.fantome_bleu.move()

    def move_down(self, event):
        self.pacman.move("bas")
        if not self.check_collision():
            self.fantome_rouge.move()
            self.fantome_jaune.move()
            self.fantome_bleu.move()

    def move_left(self, event):
        self.pacman.move("gauche")
        if not self.check_collision():
            self.fantome_rouge.move()
            self.fantome_jaune.move()
            self.fantome_bleu.move()

    def move_right(self, event):
        self.pacman.move("droite")
        if not self.check_collision():
            self.fantome_rouge.move()
            self.fantome_jaune.move()
            self.fantome_bleu.move()

    def check_collision(self):
        if (self.fantome_rouge.x, self.fantome_rouge.y) == (self.pacman.x, self.pacman.y):
            self.game_over()
            return True
        elif (self.fantome_jaune.x, self.fantome_jaune.y) == (self.pacman.x, self.pacman.y):
            self.game_over()
            return True
        elif (self.fantome_bleu.x, self.fantome_bleu.y) == (self.pacman.x, self.pacman.y):
            self.game_over()
            return True
        else:
            return False

        

if __name__ == "__main__":
        interface_game = Interface_game()