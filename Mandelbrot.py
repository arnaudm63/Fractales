# import tkinter as tk
"""
https://gist.github.com/jfpuget/60e07a82dece69b011bb
"""
import math
import pygame
import time

start = time.time()

canvas_w = 900
canvas_h = 750
iteration = 50
zoom = 1.4

# Initialisation et création d'une fenêtre aux dimensions spécifiéés munie d'un titre
pygame.init()
screen = pygame.display.set_mode((canvas_w, canvas_h))
pygame.display.set_caption("Fractale de Mandelbrot")

def add_complex(x, y):
    return (x[0] + y[0], x[1] + y[1])
def multi_complex(x, y):
    a, b = x
    c, d = y
    new_x = (a * c) - (b * d)
    new_y = (a * d) + (b * c)
    return (new_x, new_y)

def f_de_z(z, c):
    return add_complex(multi_complex(z, z), c)

def convert_pix2c(pix):
    l = 3
    h = 2.5
    xc = (pix[0] - canvas_w * (l - 1) / l) / (canvas_w / l)
    yc = (canvas_h / 2 - pix[1]) / (canvas_h / h)
    return (xc, yc)

def module(z):
    a, b = z
    return a ** 2 + b ** 2

def main():
    global iteration
    for i in range(canvas_w + 1):
        if i % (canvas_w / 10) == 0:
            print(i / (canvas_w / 100), "%")
        for j in range(canvas_h + 1):
            z = (0, 0)
            c = (i, j)
            c = convert_pix2c(c)
            n = 0
            while (module(z) < 4) and (n < iteration):
                z = f_de_z(z, c)
                n += 1
            if n == iteration:
                color = (0, 0, 0)
            else:
                #rouge, vert, bleu = 3, 1, 10# orig
                rouge, vert, bleu = 1, 4, 10
                color = ((rouge * n) % 256, (vert * n) % 256, (bleu * n) % 256)
            screen.set_at((i, j), color)
    print(time.time() - start)

    pygame.display.flip()

    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Pour quitter l'application en fermant la fenêtre
                loop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(f'Mouse clicked at {x}, {y}')
                c = convert_pix2c([x,y])
                print(f'C vaut {c[0]}, {c[1]}')
      
    pygame.quit()

if __name__ == "__main__":
    main()
