import calcul

def draw_1_triangle(canvas, triangle):
    x1, y1 = triangle[0]
    x2, y2 = triangle[1]
    x3, y3 = triangle[2]
    cercle = calcul.triangle_cercle(triangle)
    # draw_cercle(canvas, cercle)
    canvas.create_line(x1, y1, x2, y2, x2, y2, x3, y3, x1, y1, x3, y3, fill="blue")

def draw_triangles(canvas, triangles):
    for triangle in triangles:
        draw_1_triangle(canvas, triangle)
        cercle = calcul.triangle_cercle(triangle)
        # draw_cercle(canvas, cercle)
        
def draw_points(canvas, points):
    canvas.delete("all")  # Clear canvas
    for point in points:
        x, y = point
        size = 2
        canvas.create_oval(x - size, y - size, x + size, y + size, fill="red")

def draw_cercle(canvas, cercle):
    point, rayon = cercle
    xc, yc = point
    canvas.create_oval(xc - rayon, yc - rayon, xc + rayon, yc + rayon)

