import enum
import logging
import numpy as np
from geometric_objects import Triangulation, Triangle, Point, points_to_numpy_array, triangle_area


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

def is_point_in_circumcircle(vertices: list[Point], checked_point: Point) -> bool:
    circumcircle_matrix = np.ones((3, 3))
    vertices_matrix = np.ones((3, 3))
    vertices_matrix[:, 1:] = points_to_numpy_array(vertices)
    circumcircle_matrix[:, :2] = vertices_matrix[:, 1:] - points_to_numpy_array([checked_point])
    circumcircle_matrix[:, -1] = circumcircle_matrix[:, 0] ** 2 + circumcircle_matrix[:, 1] ** 2
    return -1 * np.linalg.det(vertices_matrix) * np.linalg.det(circumcircle_matrix) < 0

def is_point_in_triangle(vertices: list[Point], checked_point: Point) -> bool:
    area_abc = triangle_area(vertices)
    area_abd = triangle_area([vertices[0], vertices[1], checked_point])
    area_acd = triangle_area([vertices[0], vertices[2], checked_point])
    area_bcd = triangle_area([vertices[1], vertices[2], checked_point])
    return area_abc == area_abd + area_acd + area_bcd

def incremental_delauney_algorithm(triangulation: Triangulation) -> list[Triangle]:
    logging.getLogger().info("Incremental triangulation algorithm is not implemented yet.")
    return triangulation.triangles

def flipping_delauney_algorithm(triangulation: Triangulation) -> list[Triangle]:
    logging.getLogger().info("Flipping triangulation algorithm is not implemented yet.")
    return triangulation.triangles