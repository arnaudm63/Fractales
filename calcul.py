import random
from math import *
#
# Variables Globales
#
num_points = 6
canvas_width = 600
canvas_height = 600
triangles = []

def generate_random_points(num_points):
    global canvas_width
    global canvas_height
    points = []
    for _ in range(num_points):
        x = random.randint(10, canvas_width - 10)
        y = random.randint(10, canvas_height - 10)
        points.append((x, y))
    return points

def ajout_super_triangle(points):
    global canvas_width
    global canvas_height
    x_min = canvas_width
    y_min = canvas_height
    x_max = 0
    y_max = 0
    for point in points:
        x, y = point
        if x < x_min:
            x_min = x
        if y < y_min:
            y_min = y
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y
    p0 = x_min - 5, y_min - 5
    p1 = x_min - 5, y_max * 2 - y_min + 10
    p2 = x_max * 2 - x_min + 10, y_min - 5
    super_triangle = [p0, p1, p2]
    # print(super_triangle)
    return super_triangle

def generate_triangles(points):
    global triangles
    triangles = []
    tri = ajout_super_triangle(points)
    # print(tri)
    triangles += [tri]
    num_points = len(points)
    for i in range(0, num_points - 2):
        for j in range(i + 1, num_points - 1):
            for k in range(j + 1, num_points):
                tri = [points[i], points[j], points[k]]
                # print(tri)
                triangles += [tri]
                # print(i+1, j+1, k+1)
    print(len(triangles))
    return triangles

def signe(triangle):
    pt1 = triangle[0]
    pt2 = triangle[1]
    pt3 = triangle[2]
    produit = (pt1[0] - pt3[0]) * (pt2[1] - pt3[1]) - (pt2[0] - pt3[0]) * (pt1[1] - pt3[1])
    return produit

def pt_dans_triangle(point, triangle):
    test_tri1 =(point, triangle[0], triangle[1]) 
    test_tri2 =(point, triangle[1], triangle[2]) 
    test_tri3 =(point, triangle[2], triangle[0]) 
    d1 = signe(test_tri1)
    d2 = signe(test_tri2)
    d3 = signe(test_tri3)
    cpt_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    cpt_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    return not(cpt_neg and cpt_pos)

def triangle_cercle(triangle):
    x1, y1 = triangle[0]
    x2, y2 = triangle[1]
    x3, y3 = triangle[2]
    terme1 = (x3 * x3 - x2 * x2 + y3 * y3 - y2 * y2) / (2 * (y3 - y2))
    terme2 = (x2 * x2 - x1 * x1 + y2 * y2 - y1 * y1) / (2 * (y2 - y1))
    terme3 = ((x3 - x2) / (y3 - y2)) - ((x2 - x1) / (y2 - y1))
    xc = (terme1 - terme2) / terme3
    yc = ((x1 - x2) / (y2 - y1)) * xc + (x2 * x2 - x1 * x1 + y2 * y2 - y1 * y1) / (2 * (y2 - y1))
    centre = xc, yc
    rayon = sqrt((x1 - xc) * (x1 - xc) + (y1 - yc) * (y1 - yc))
    cercle = centre, rayon
    return cercle

def cree_3_triangles(point, triangle):
    new_tri = []
    for i in range(2):
        new_tri += [point, triangle[i]]
    return new_tri

def procede_points(points, triangles):
    for i in points:
        for j in triangles:
            resultat = pt_dans_triangle(i, j)

def test_pt_dans_cercle(points, cercle):
    xc, yc, rayon = cercle
    cpt = 0
    for p in points:
        x, y = p
        longueur_p=sqrt((x - xc) * (x - xc) + (y - yc)* (y - yc))
        if (longueur_p >= rayon):
            cpt += 1
    if cpt == 0:
        return True
    else:
        return False