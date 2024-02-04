from tkinter import *
import random
##constante--------
GAME_LARGEUR = 700
Game_HAUTEUR = 700
SPEED = 70
TAILLE = 50
CORPS_SERPANT = 3
COULEUR_SERPENT = "#FFFFFF"
COULEUR_FRUIT = "#FF00FF"
BACKGROUND = "#000000"


##------------------------------------------------------------------------------
##Classes
class Serpent():
    def __init__(self):
        self.taille_du_corps = CORPS_SERPANT
        self.coordinates = []
        self.square = []

        for i in range(0, CORPS_SERPANT):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canva.create_rectangle(x, y, x + TAILLE, y + TAILLE, fill=COULEUR_SERPENT, tag="serpent")
            self.square.append(square)


class Fruit():

    def __init__(self):
        x = random.randint(0, (GAME_LARGEUR / TAILLE) - 1) * TAILLE
        y = random.randint(0, (Game_HAUTEUR / TAILLE) - 1) * TAILLE

        self.coordinates = [x, y]
        canva.create_oval(x, y, x + TAILLE, y + TAILLE, fill=COULEUR_FRUIT, tag="food")


##------------------------------------------------------------------------------
##Fonctions
def collision(serpent):
    x,y = serpent.coordinates[0]
    if x < 0 or  x >= GAME_LARGEUR:
        return True

    elif y < 0 or  y >= Game_HAUTEUR:
        return True
    for i in serpent.coordinates[1:]:
        if x == i[0] and y == i[1]:
            return True
    return False
def round(serpent, fruit):
    x, y = serpent.coordinates[0]

    if direction == "up":
        y -= TAILLE
    elif direction == "down":
        y += TAILLE
    elif direction == "left":
        x -= TAILLE
    elif direction == "right":
        x += TAILLE

    serpent.coordinates.insert(0, (x, y))

    square = canva.create_rectangle(x, y, x + TAILLE, y + TAILLE, fill=COULEUR_SERPENT)

    serpent.square.insert(0, square)
    if x == fruit.coordinates[0] and y == fruit.coordinates[1]:
        global score
        score +=1
        label.config(text="Score :{}".format(score))
        canva.delete("food")
        fruit = Fruit()
    else:
        del serpent.coordinates[-1]
        canva.delete(serpent.square[-1])
        del serpent.square[-1]
    if collision(serpent):
        gameover()
    else:
        fenêtre.after(SPEED, round, serpent, fruit)

def nvdirection(nvldirection):
    global direction

    if nvldirection == 'left' :
        if direction != 'right':
            direction = nvldirection
    elif nvldirection == 'right':
        if direction != 'left':
            direction = nvldirection
    elif nvldirection == 'up' :
        if direction != 'down':
            direction = nvldirection
    elif nvldirection == 'down':
        if direction != 'up':
            direction = nvldirection

def gameover():
    canva.delete(ALL)
    canva.create_text(canva.winfo_width()/2,canva.winfo_height()/2,font=('arial',50),text="GAME OVER",fill="purple",tag="gameover")


##------------------------------------------------------------------------------
##Fenêtre
fenêtre = Tk()
fenêtre.title("Snake Game")
score = 0
direction = 'down'

label = Label(fenêtre, text="Score :{}".format(score), font=('consolas', 40))
label.pack()
canva = Canvas(fenêtre, bg=BACKGROUND, height=Game_HAUTEUR, width=GAME_LARGEUR)
canva.pack()
fenêtre.update()
fenêtre_l = fenêtre.winfo_width()
fenêtre_h = fenêtre.winfo_height()
ecranw = fenêtre.winfo_screenwidth()
ecranh = fenêtre.winfo_screenheight()
x = int(ecranw / 2 - fenêtre_l / 2)
y = int(ecranh / 2 - fenêtre_h / 2)
fenêtre.geometry(f"{fenêtre_l}x{fenêtre_h}+{x}+{y}")
fenêtre.bind('<Left>',lambda event: nvdirection('left'))
fenêtre.bind('<Right>',lambda event: nvdirection('right'))
fenêtre.bind('<Up>',lambda event: nvdirection('up'))
fenêtre.bind('<Down>',lambda event: nvdirection('down'))
##------------------------------------------------------------------------------
##Main game()
serpent = Serpent()
fruits = Fruit()
round(serpent,fruits)
fenêtre.mainloop()
