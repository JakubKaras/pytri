from geometric_objects import Triangulation, Point, Triangle
import numpy as np
import matplotlib.pyplot as plt
from convex_hull_triangulation import Convex_hull_triangulation, Point_list_to_npArray_converter

class flipping_delaunay:
    def calculate_triangulation(self, triangulation: Triangulation):
        a = 42

points = [Point(-0.5,-0.5), Point(0,0), Point(1,0), Point(1,1), Point(0,1), Point(0.2, 0.8),Point(0.3, 0.3), Point(0.5, 0.5)]
pointsNp = Point_list_to_npArray_converter().list_of_points_to_nparray(points)
trian = Convex_hull_triangulation().calculate_triangulation(points)
plt.figure()
plt.plot(pointsNp[:,0], pointsNp[:,1], 'ro')

for triangle in trian:
    plt.plot([pointsNp[triangle.point_index1, 0], pointsNp[triangle.point_index2, 0]], [pointsNp[triangle.point_index1, 1], pointsNp[triangle.point_index2, 1]])
    plt.plot([pointsNp[triangle.point_index1, 0], pointsNp[triangle.point_index3, 0]], [pointsNp[triangle.point_index1, 1], pointsNp[triangle.point_index3, 1]])
    plt.plot([pointsNp[triangle.point_index3, 0], pointsNp[triangle.point_index2, 0]], [pointsNp[triangle.point_index3, 1], pointsNp[triangle.point_index2, 1]])


plt.show()


