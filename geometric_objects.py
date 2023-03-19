'''Geometric objects and their manipulation.'''
from dataclasses import dataclass
import numpy as np

@dataclass
class Point:
    x: float
    y: float

    def __eq__(self, other):
        return (
            self.__class__ is other.__class__
            and self.x == other.x
            and self.y == other.y
        )

    def to_tuple(self):
        return self.x, self.y

@dataclass
class Triangle:
    point_index1: int
    point_index2: int
    point_index3: int

    def to_list(self):
        return [self.point_index1, self.point_index2, self.point_index3]

@dataclass
class Triangulation:
    points:  list[Point]
    triangles: list[Triangle]

    def distance_point_to_triangulation(self, outside_point: Point):
        '''Take the minimal distance from distances to all points of triangulation to `outside_point`.'''
        min_distance = np.infty
        for triangulation_point in self.points:
            distance = distance_point_to_point(triangulation_point, outside_point)
            if distance < min_distance:
                min_distance = distance
        return min_distance

    def check_circumcircle_of_triangle(self, checked_triangle: Triangle, point_not_on_side_index: int):
        """Performs check (and corrects if needed) whether or not circumcircle of `checked_triangle` contains fourth point.
        The fourth point is obtained in following way:
            Take the side of `checked_triangle` that doesn't contain `point_not_on_side_index`, find triangle containing the same side and the third vertex is our fourth point.

        Args:
            checked_triangle (Triangle): triangle we wish to check
            point_not_on_side_index (int): index of vertex of `checked_triangle`
        """        
        checked_triangle_index = self.triangles.index(checked_triangle)
        points_on_line = [x for x in checked_triangle.to_list() if x != point_not_on_side_index]
        # find the opposite point
        opposite_point_index = None
        for index, triangle in enumerate(self.triangles):
            if checked_triangle_index != index and set(points_on_line).issubset(set(triangle.to_list())):
                opposite_triangle_index = index
                opposite_point_index = list(set(triangle.to_list()).difference(set(points_on_line)))[0]
                break
        # check if the line is on the boundary
        if opposite_point_index is None:
            return
        # check if the opposite point is in the triangle's circumcircle
        if not is_point_in_circumcircle([self.points[i] for i in checked_triangle.to_list()], self.points[opposite_point_index]):
            return
        # if it is, flip side
        del self.triangles[max(checked_triangle_index, opposite_triangle_index)]
        del self.triangles[min(checked_triangle_index, opposite_triangle_index)]
        new_triangle_1 = Triangle(points_on_line[0], point_not_on_side_index, opposite_point_index)
        new_triangle_2 = Triangle(points_on_line[1], point_not_on_side_index, opposite_point_index)
        self.triangles.append(new_triangle_1)
        self.triangles.append(new_triangle_2)
        # check the new triangles
        self.perform_circumcircle_check_for_all_vertices(new_triangle_1)
        self.perform_circumcircle_check_for_all_vertices(new_triangle_2)

    def perform_circumcircle_check_for_all_vertices(self, triangle: Triangle):
        for point in triangle.to_list():
            if triangle not in self.triangles:
                break
            self.check_circumcircle_of_triangle(triangle, point)

def is_point_in_circumcircle(vertices: list[Point], checked_point: Point) -> bool:
    '''Check whether or not is `checked_point` in circumcircle of triangle defined by `vertices`.'''
    circumcircle_matrix = np.ones((3, 3))
    vertices_matrix = np.ones((3, 3))
    vertices_matrix[:, 1:] = points_to_numpy_array(vertices)
    circumcircle_matrix[:, :2] = vertices_matrix[:, 1:] - points_to_numpy_array([checked_point])
    circumcircle_matrix[:, -1] = circumcircle_matrix[:, 0] ** 2 + circumcircle_matrix[:, 1] ** 2
    return -1 * np.linalg.det(vertices_matrix) * np.linalg.det(circumcircle_matrix) < 0

def is_point_in_triangle(vertices: list[Point], checked_point: Point) -> bool:
    '''Check whether or not is `checked_point` in triangle defined by `vertices`.'''
    area_abc = triangle_area(vertices)
    area_abd = triangle_area([vertices[0], vertices[1], checked_point])
    area_acd = triangle_area([vertices[0], vertices[2], checked_point])
    area_bcd = triangle_area([vertices[1], vertices[2], checked_point])
    return area_abc == area_abd + area_acd + area_bcd

def triangle_area(vertices: list[Point]):
    return abs((vertices[0].x * (vertices[1].y - vertices[2].y) + vertices[1].x * (vertices[2].y - vertices[0].y)
                + vertices[2].x * (vertices[0].y - vertices[1].y)) / 2.0)

def distance_point_to_point(a: Point, b: Point):
    return np.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

def points_to_numpy_array(points: list[Point]) -> np.array:
    x_coordinates = [point.x for point in points]
    y_coordinates = [point.y for point in points]
    return np.array([x_coordinates, y_coordinates]).T