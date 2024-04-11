import tkinter as tk
import random
import math

def generate_points_3d(num_points):
    points = [(random.randint(50, 550), random.randint(50, 350), random.randint(0, 200)) for _ in range(num_points)]
    return points

def draw_delaunay_3d(canvas, points):
    triangles = delaunay_triangulation_3d(points)
    for triangle in triangles:
        p0, p1, p2 = triangle
        canvas.create_line(points[p0][0], points[p0][1], points[p0][2], 
                           points[p1][0], points[p1][1], points[p1][2], fill="blue")
        canvas.create_line(points[p1][0], points[p1][1], points[p1][2], 
                           points[p2][0], points[p2][1], points[p2][2], fill="blue")
        canvas.create_line(points[p2][0], points[p2][1], points[p2][2], 
                           points[p0][0], points[p0][1], points[p0][2], fill="blue")

def delaunay_triangulation_3d(points):
    def circumcircle_radius_3d(p0, p1, p2):
        ax, ay, az = p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2]
        bx, by, bz = p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2]
        cx, cy, cz = ax * (p0[0] + p1[0]) + ay * (p0[1] + p1[1]) + az * (p0[2] + p1[2]), \
                     bx * (p0[0] + p2[0]) + by * (p0[1] + p2[1]) + bz * (p0[2] + p2[2]), \
                     (ax * ax + ay * ay + az * az) * (bx * by - by * bz) - (bx * bx + by * by + bz * bz) * (ax * ay - ay * az)
        x = (by * cx - ay * cy) / cz
        y = (ax * cy - bx * cx) / cz
        z = 0.5 * math.sqrt((p0[0] - x) ** 2 + (p0[1] - y) ** 2 + (p0[2] - z) ** 2)
        return z, (x, y, z)

    def in_circumcircle_3d(p0, p1, p2, p):
        r, (cx, cy, cz) = circumcircle_radius_3d(p0, p1, p2)
        return math.sqrt((p[0] - cx) ** 2 + (p[1] - cy) ** 2 + (p[2] - cz) ** 2) <= r

    def delaunay_triangulation_rec_3d(points, indices):
        if len(indices) <= 3:
            return [tuple(indices)]

        p0, p1, p2 = points[indices[0]], points[indices[1]], points[indices[2]]
        triangles = []
        for i in range(3, len(indices)):
            p = points[indices[i]]
            if in_circumcircle_3d(p0, p1, p2, p):
                new_triangles = delaunay_triangulation_rec_3d(points, [indices[0], indices[1], indices[i]]) + \
                                delaunay_triangulation_rec_3d(points, [indices[1], indices[2], indices[i]]) + \
                                delaunay_triangulation_rec_3d(points, [indices[2], indices[0], indices[i]])
                triangles.extend(new_triangles)
                return triangles
        triangles.append((indices[0], indices[1], indices[2]))
        new_triangles = delaunay_triangulation_rec_3d(points, [indices[0], indices[2], indices[3]])
        triangles.extend(new_triangles)
        return triangles

    # Create a super triangle that contains all the points
    min_x = min(point[0] for point in points)
    min_y = min(point[1] for point in points)
    min_z = min(point[2] for point in points)
    max_x = max(point[0] for point in points)
    max_y = max(point[1] for point in points)
    max_z = max(point[2] for point in points)
    super_triangle = [(min_x - 10, min_y - 10, min_z - 10), 
                      (max_x + 10, min_y - 10, min_z - 10), 
                      (max_x / 2, max_y + 10, max_z + 10)]

    # Perform Delaunay triangulation
    indices = list(range(len(points)))
    triangles = delaunay_triangulation_rec_3d(points + super_triangle, indices)

    # Remove triangles that contain any vertex from the super triangle
    triangles = [triangle for triangle in triangles if not any(index >= len(points) for index in triangle)]
    
    return [(triangle[0], triangle[1], triangle[2]) for triangle in triangles]

def main():
    root = tk.Tk()
    root.title("Delaunay Triangulation in 3D")
    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.pack()

    points = generate_points_3d(10)
    draw_delaunay_3d(canvas, points)

    root.mainloop()

if __name__ == "__main__":
    main()
