import tkinter as tk
import math

w = 600
h = 600
order = 0
size = 450

def trace_ligne(canvas, pt_A, pt_B):
    xA, yA = pt_A
    xB, yB = pt_B
    canvas.create_line(xA, yA, xB, yB, fill = "blue")

def curve_koch(canvas, order, size, pt_A, pt_B):
    xA, yA = pt_A
    xB, yB = pt_B
    if order == 0:
        trace_ligne(canvas, pt_A, pt_B)
    else:
        dx = xB - xA
        dy = yB - yA
        distance = math.sqrt(dx**2 + dy**2)
        unit = (dx / distance, dy / distance)
        xC = xA + unit[0] * distance / 3
        yC = yA + unit[1] * distance / 3
        pt_C = xC, yC
        
        xD = xA + unit[0] * distance / 2 - unit[1] * distance / (2 * math.sqrt(3))
        yD = yA + unit[1] * distance / 2 + unit[0] * distance / (2 * math.sqrt(3))
        pt_D = xD, yD
        
        xE = xA + unit[0] * 2 * distance / 3
        yE = yA + unit[1] * 2 * distance / 3
        pt_E = xE, yE
        
        curve_koch(canvas, order - 1, size, pt_A, pt_C)
        curve_koch(canvas, order - 1, size, pt_C, pt_D)
        curve_koch(canvas, order - 1, size, pt_D, pt_E)
        curve_koch(canvas, order - 1, size, pt_E, pt_B)
        
def flocon_koch(order, size, canvas):
    x1 = w / 2 + size / 2
    y1 = h / 2 + size * math.sqrt(3) / 6
    x2 = w / 2
    y2 = h / 2 - size * math.sqrt(3) / 3
    x3 = w / 2 - size / 2
    y3 = h / 2 + size * math.sqrt(3) / 6
    pt1 = x1, y1
    pt2 = x2, y2
    pt3 = x3, y3
    
    curve_koch(canvas, order, size, pt1, pt2)
    curve_koch(canvas, order, size, pt2, pt3)
    curve_koch(canvas, order, size, pt3, pt1)

def regen(size, canvas):
    global order
    canvas.delete("all")
    flocon_koch(order, size, canvas)
    # print(order)
    order += 1
    if order == 7:
        order = 0

def main():
    root = tk.Tk()
    root.title("Flocon de Koch")
    global order
    
    canvas = tk.Canvas(root, width=w, height=h, bg="white")
    canvas.pack()
    print(order)

    regen(size, canvas)

    def on_click(event):
        regen(size, canvas)

    canvas.bind("<Button-1>", on_click)

    root.mainloop()

if __name__ == "__main__":
    main()
