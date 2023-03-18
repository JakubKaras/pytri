'''Geometric objects and their manipulation.'''
from dataclasses import dataclass
import numpy as np
import enum
import logging


class AlgorithmEnum(enum.Enum):
    FLIPPING = 'Flipping'
    INCREMENTAL = 'Incremental'


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

    def add_point(self, point: Point, triangulation_algorithm: AlgorithmEnum, min_distance = 20):
        if self.distance_point_to_triangulation(point) >= min_distance:
            self.points.append(point)
            self.point_triplets = compute_triangulation(self, triangulation_algorithm)

    def distance_point_to_triangulation(self, outside_point: Point):
        '''Take the minimal distance from distances to all points of triangulation to `outside_point`.'''
        min_distance = np.infty
        for triangulation_point in self.points:
            distance = distance_point_to_point(triangulation_point, outside_point)
            if distance < min_distance:
                min_distance = distance
        return min_distance

def distance_point_to_point(a: Point, b: Point):
    return np.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

def points_to_numpy_array(points: list[Point]) -> np.array:
    x_coordinates = [point.x for point in points]
    y_coordinates = [point.y for point in points]
    return np.array([x_coordinates, y_coordinates]).T

def compute_triangulation(triangulation: Triangulation, triangulation_algorithm: AlgorithmEnum) -> list[Triangle]:
    if triangulation_algorithm == AlgorithmEnum.FLIPPING:
        return flipping_delauney_algorithm(triangulation)
    if triangulation_algorithm == AlgorithmEnum.INCREMENTAL:
        return incremental_delauney_algorithm(triangulation)

def incremental_delauney_algorithm(triangulation: Triangulation) -> list[Triangle]:
    logging.getLogger().info("Incremental triangulation algorithm is not implemented yet.")
    return triangulation.point_triplets

def flipping_delauney_algorithm(triangulation: Triangulation) -> list[Triangle]:
    logging.getLogger().info("Flipping triangulation algorithm is not implemented yet.")
    return triangulation.point_triplets