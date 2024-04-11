import tkinter as tk
import random

w = 800
h = 600
size = 200
taille_grille = (w / size, h  / size)

def genere(taille_grille):
    taux = 0.1
    x, y = taille_grille
    grille = []
    for i in range(int(x)):
        for j in range(int(y)):
            # grille[i, j] = round(random(1), 0)
            grille[i, j] += [0]

def test(taille_grille, grille):
    x, y = taille_grille
    for i in range(3, -1):
        for j in range(3, -1):
            print(i, j)

def affiche(canvas, gen):
    global taille_grille
    grille = genere(taille_grille)
    test(taille_grille, grille)

def main():
    root = tk.Tk()
    root.title("Jeu de la Vie")
    
    canvas = tk.Canvas(root, width=w, height=h, bg="white")
    canvas.pack()

    gen = 0
    affiche(canvas, gen)

    while True:
        gen += 1
        affiche(canvas, gen)

    root.mainloop()

if __name__ == "__main__":
    main()
    