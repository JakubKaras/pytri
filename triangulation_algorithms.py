import enum
import logging
import numpy as np
from geometric_objects import Triangulation, Triangle, Point, points_to_numpy_array, is_point_in_triangle 


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
    # add triangle containing all points
    expanded_triangulation = expand_triangulation(triangulation)
    not_added_points = [x for x in range(len(triangulation.points))]
    while len(not_added_points) > 0:
        # choose random point to be added to triangulation
        rnd_index = np.random.choice(len(not_added_points))
        adding_point_at_index = not_added_points[rnd_index]
        # find triangle containing this point
        triangle_index = [
                is_point_in_triangle(
                [expanded_triangulation.points[i] for i in triangle.to_list()],
                expanded_triangulation.points[adding_point_at_index]
            ) for triangle in expanded_triangulation.triangles
        ].index(True)
        triangle_vertices_indices = expanded_triangulation.triangles[triangle_index]
        # create lines to vertices of the triangle from the point
        expanded_triangulation.triangles.append(Triangle(triangle_vertices_indices.point_index1, triangle_vertices_indices.point_index2, adding_point_at_index))
        expanded_triangulation.triangles.append(Triangle(triangle_vertices_indices.point_index1, triangle_vertices_indices.point_index3, adding_point_at_index))
        expanded_triangulation.triangles.append(Triangle(triangle_vertices_indices.point_index2, triangle_vertices_indices.point_index3, adding_point_at_index))
        # delete the triangle containing the point in its interior
        del expanded_triangulation.triangles[triangle_index]
        # check circumcircles
        # delete from `not_added_points`
        del not_added_points[rnd_index]
    # remove triangles containing the big triangle
    remove_triangles_at = []
    for i, triangle in enumerate(expanded_triangulation.triangles):
        for outer_point in range(len(expanded_triangulation.points) - 3, len(expanded_triangulation.points)):
            if outer_point in triangle.to_list():
                remove_triangles_at.append(i)
    for index in sorted(set(remove_triangles_at), reverse=True):
        del expanded_triangulation.triangles[index]
    return triangulation.triangles # TODO return correct triangles

def expand_triangulation(triangulation: Triangulation) -> Triangulation:
    '''Adds a triangle containing all points in `triangulation`.'''
    vertices_matrix = points_to_numpy_array(triangulation.points)
    max_coordinate_values = np.max(vertices_matrix, axis=0)
    outer_vertices = [
        Point(max_coordinate_values[0] + 150, max_coordinate_values[1] + 150),
        Point(max_coordinate_values[0] + 150, -max_coordinate_values[1] - 300),
        Point(-max_coordinate_values[0] - 300, max_coordinate_values[1] + 150)
    ]
    num_of_points = vertices_matrix.shape[0] + 3
    expanded_triangulation = Triangulation([*triangulation.points, *outer_vertices], [Triangle(num_of_points - 3, num_of_points - 2, num_of_points - 1)])
    return expanded_triangulation

def flipping_delauney_algorithm(triangulation: Triangulation) -> list[Triangle]:
    logging.getLogger().info("Flipping triangulation algorithm is not implemented yet.")
    return triangulation.triangles