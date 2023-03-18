'''Data classes for moving data around'''
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
    point_triplets: list[Triangle]

def points_to_numpy_array(points: list[Point]) -> np.array:
    x_coordinates = [point.x for point in points]
    y_coordinates = [point.y for point in points]
    return np.array([x_coordinates, y_coordinates]).T