'''Data classes for moving data around'''
from dataclasses import dataclass

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