import enum
import logging
from geometric_objects import Triangulation, Triangle, Point


class AlgorithmEnum(enum.Enum):
    FLIPPING = 'Flipping'
    INCREMENTAL = 'Incremental'

def add_point_to_triangulation(triangulation: Triangulation, point: Point, triangulation_algorithm: AlgorithmEnum, min_distance = 20):
    new_points = triangulation.points.copy()
    new_triangles = triangulation.triangles.copy()
    if triangulation.distance_point_to_triangulation(point) >= min_distance:
        new_points.append(point)
        new_triangles = compute_triangles(Triangulation(new_points, new_triangles), triangulation_algorithm)
    return Triangulation(new_points, new_triangles)

def compute_triangles(triangulation: Triangulation, triangulation_algorithm: AlgorithmEnum) -> list[Triangle]:
    if len(triangulation.points) < 3:
        return []
    if len(triangulation.points) == 3:
        return [Triangle(0, 1, 2)]
    if triangulation_algorithm == AlgorithmEnum.FLIPPING:
        return flipping_delauney_algorithm(triangulation)
    if triangulation_algorithm == AlgorithmEnum.INCREMENTAL:
        return incremental_delauney_algorithm(triangulation)
    raise ValueError(f"{triangulation_algorithm} is not supported.")

def incremental_delauney_algorithm(triangulation: Triangulation) -> list[Triangle]:
    logging.getLogger().info("Incremental triangulation algorithm is not implemented yet.")
    return triangulation.triangles

def flipping_delauney_algorithm(triangulation: Triangulation) -> list[Triangle]:
    logging.getLogger().info("Flipping triangulation algorithm is not implemented yet.")
    return triangulation.triangles