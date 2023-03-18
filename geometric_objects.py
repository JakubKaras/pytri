'''Data classes for moving data around'''
from dataclasses import dataclass
import numpy as np

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Triangle:
    point_index1: int
    point_index2: int
    point_index3: int

@dataclass
class Triangulation:
    points:  list[Point]
    point_triplets: list[Triangle]

def points_to_numpy_array(points: list[Point]) -> np.array:
    x_coordinates = [point.x for point in points]
    y_coordinates = [point.y for point in points]
    return np.array([x_coordinates, y_coordinates]).T
