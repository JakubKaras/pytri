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

def triangle_area(vertices: list[Point]):
    return abs((vertices[0].x * (vertices[1].y - vertices[2].y) + vertices[1].x * (vertices[2].y - vertices[0].y)
                + vertices[2].x * (vertices[0].y - vertices[1].y)) / 2.0)

def distance_point_to_point(a: Point, b: Point):
    return np.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

def points_to_numpy_array(points: list[Point]) -> np.array:
    x_coordinates = [point.x for point in points]
    y_coordinates = [point.y for point in points]
    return np.array([x_coordinates, y_coordinates]).T