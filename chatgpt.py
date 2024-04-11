import tkinter as tk
import random
import math

def generate_points(canvas, num_points):
    points = [(random.randint(50, 550), random.randint(50, 350)) for _ in range(num_points)]
    for point in points:
        canvas.create_oval(point[0]-3, point[1]-3, point[0]+3, point[1]+3, fill="red")
    return points

def draw_delaunay(canvas, points):
    triangles = delaunay_triangulation(points)
    for triangle in triangles:
        p0, p1, p2 = triangle
        canvas.create_line(points[p0][0], points[p0][1], points[p1][0], points[p1][1], fill="blue")
        canvas.create_line(points[p1][0], points[p1][1], points[p2][0], points[p2][1], fill="blue")
        canvas.create_line(points[p2][0], points[p2][1], points[p0][0], points[p0][1], fill="blue")

def delaunay_triangulation(points):
    def circumcircle_radius(p0, p1, p2):
        dx, dy = p1[0] - p0[0], p1[1] - p0[1]
        ex, ey = p2[0] - p0[0], p2[1] - p0[1]
        bl = dx * (p0[0] + p1[0]) + dy * (p0[1] + p1[1])
        cl = ex * (p0[0] + p2[0]) + ey * (p0[1] + p2[1])
        d = 2 * (dx * (p2[1] - p1[1]) - dy * (p2[0] - p1[0]))
        x = (ey * bl - dy * cl) / d
        y = (dx * cl - ex * bl) / d
        return math.sqrt((p0[0] - x) ** 2 + (p0[1] - y) ** 2), (x, y)

    def in_circumcircle(p0, p1, p2, p):
        r, (cx, cy) = circumcircle_radius(p0, p1, p2)
        return math.sqrt((p[0] - cx) ** 2 + (p[1] - cy) ** 2) <= r

    def delaunay_triangulation_rec(points, indices):
        if len(indices) <= 3:
            return [tuple(indices)]

        p0, p1, p2 = points[indices[0]], points[indices[1]], points[indices[2]]
        triangles = []
        for i in range(3, len(indices)):
            p = points[indices[i]]
            if in_circumcircle(p0, p1, p2, p):
                new_triangles = delaunay_triangulation_rec(points, [indices[0], indices[1], indices[i]]) + \
                                delaunay_triangulation_rec(points, [indices[1], indices[2], indices[i]]) + \
                                delaunay_triangulation_rec(points, [indices[2], indices[0], indices[i]])
                triangles.extend(new_triangles)
                return triangles
        triangles.append((indices[0], indices[1], indices[2]))
        new_triangles = delaunay_triangulation_rec(points, [indices[0], indices[2], indices[3]])
        triangles.extend(new_triangles)
        return triangles

    # Create a super triangle that contains all the points
    min_x = min(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_x = max(point[0] for point in points)
    max_y = max(point[1] for point in points)
    super_triangle = [(min_x - 10, min_y - 10), (max_x + 10, min_y - 10), (max_x / 2, max_y + 10)]

    # Perform Delaunay triangulation
    indices = list(range(len(points)))
    triangles = delaunay_triangulation_rec(points + super_triangle, indices)

    # Remove triangles that contain any vertex from the super triangle
    triangles = [triangle for triangle in triangles if not any(index >= len(points) for index in triangle)]
    
    return [(triangle[0], triangle[1], triangle[2]) for triangle in triangles]

def main():
    root = tk.Tk()
    root.title("Delaunay Triangulation")
    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.pack()

    points = generate_points(canvas, 10)
    draw_delaunay(canvas, points)

    root.mainloop()

if __name__ == "__main__":
    main()
