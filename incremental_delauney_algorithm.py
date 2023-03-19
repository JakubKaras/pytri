import logging
import numpy as np
from geometric_objects import Triangulation, Triangle, Point, is_point_in_triangle, points_to_numpy_array

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
        triangles_to_check = [expanded_triangulation.triangles[-3], expanded_triangulation.triangles[-2], expanded_triangulation.triangles[-1]]
        for triangle in triangles_to_check:
            expanded_triangulation.check_circumcircle_of_triangle(triangle, adding_point_at_index)
        # delete from `not_added_points`
        del not_added_points[rnd_index]
    # remove triangles containing at least two vetrices of the big triangle
    triangles = remove_expansion_triangles(expanded_triangulation)
    return triangles

def remove_expansion_triangles(triangulation: Triangulation) -> list[Triangle]:
    remove_triangles_at = []
    outer_points = set([x for x in range(len(triangulation.points) - 3, len(triangulation.points))])
    for i, triangle in enumerate(triangulation.triangles):
        if len(outer_points.intersection(triangle.to_list())) >= 2:
            remove_triangles_at.append(i)
    for index in sorted(set(remove_triangles_at), reverse=True):
        del triangulation.triangles[index]
    return triangulation.triangles

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
