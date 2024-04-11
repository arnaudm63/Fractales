import tkinter as tk
import dessine
num_points = dessine.calcul.num_points
canvas_width = dessine.calcul.canvas_width
canvas_height = dessine.calcul.canvas_height
triangles = dessine.calcul.triangles

def traite_points(points, tri_tri):
    for i in points:
        j = 0
        Delaunay_tri = []
        while j < len(tri_tri):
            triangle = tri_tri[j]
            resultat = dessine.calcul.pt_dans_triangle(i, triangle)
            #  resultat = False
            if resultat == True:
                new_tri = dessine.calcul.cree_3_triangles(i, tri_tri[j])
                global triangles
                triangles += [new_tri]
                print(len(triangles))
            j += 1
    return Delaunay_tri
        
def regenerate_points(canvas, num_points):
    global canvas_width
    global canvas_height
    points = dessine.calcul.generate_random_points(num_points)
    dessine.draw_points(canvas, points)
    triangles = dessine.calcul.generate_triangles(points)
    # dessine.draw_triangles(canvas, triangles)
    Delaunay_tri = traite_points(points, triangles)
    dessine.draw_triangles(canvas, triangles)

def boucle(points):
    # génère le super_triangle dans liste vide 'triangles'
    # génère les triangles dans liste 'triangles'
    # variable 'points_a_traiter' = liste de 'points'
    # pour chaque 'point_a_traiter', rechercher dans 'triangles' le triangle qui inclue le point
    # dès que le triangle est trouvé
    #   crée 3 triangles
    #   teste si chaque triangle est Delaunay
    #       on calcule le cercle circonscrit
    #       pour chaque point on teste s'il est dans le cercle
    #       si pas de point, le triangle est Delaunay
    #       si le point est à l'intérieur, on cherche le triangle qui a 2 points communs et le point dans le cercle et on flip
    #       on reteste le triangle
    #   si oui, le triangle est rajouté dans la liste des 'triangles_Delaunay'
    #   on rajoute les triangles dans la liste des triangles
    #
    #
    #
    #
    #
    #
    return 0

def main():
    global num_points
    global canvas_width
    canvas_height = 600
    triangles = []

    root = tk.Tk()
    root.title("Random Points on Canvas")

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    regenerate_points(canvas, num_points)

    def on_click(event):
        regenerate_points(canvas, num_points)

    canvas.bind("<Button-1>", on_click)

    root.mainloop()

if __name__ == "__main__":
    main()
