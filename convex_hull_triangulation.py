from geometric_objects import Triangulation, Point, Triangle
from scipy.spatial import ConvexHull
from shapely.geometry import Point as PointShapely
from shapely.geometry.polygon import Polygon
import numpy as np

class Point_list_to_npArray_converter:
    def list_of_points_to_nparray(self, points: list[Point]):
            array = np.empty([0, 2])
            for point in points:
                array = np.append(array, [np.array([point.x, point.y])], axis=0)
            return array


class Triangulation_updater:
    def change_triangulation_according_effected_triangles(self, effected_triangles: list[Triangle], 
                                                           triangulation: list[Triangle], pointIndex) -> list[Triangle]:
        self.__remove_effected_triangles(effected_triangles, triangulation)
        new_triangles = self.__get_unique_triangles(effected_triangles, pointIndex)
        return self.__update_triangulation(triangulation, new_triangles)
    def __remove_effected_triangles(self, effected_triangles: list[Triangle], triangulation: list[Triangle]):
        for triangle in effected_triangles:
            triangulation.remove(triangle)
    def __get_unique_triangles(self, effected_triangles: list[Triangle], pointIndex) -> list[frozenset]:
        new_triangles = list()
        for triangle in effected_triangles:
            new_triangles.append(frozenset([pointIndex, triangle.point_index1, triangle. point_index2]))
            new_triangles.append(frozenset([pointIndex, triangle.point_index2, triangle. point_index3]))
            new_triangles.append(frozenset([pointIndex, triangle.point_index1, triangle. point_index3]))
        return [x for x in new_triangles if new_triangles.count(x) == 1]
    def __update_triangulation(self, triangulation: list[Triangle], new_triangles: list[frozenset]):
        for triangle_vertices in new_triangles:
            vertices = list(triangle_vertices)
            triangulation.append(Triangle(vertices[0], vertices[1], vertices[2]))
        return triangulation
          

class Convex_hull_triangulation:
    def calculate_triangulation(self, points: list[Point]):
        convex_hull = self.__calculate_convex_hull(points)
        initial_triangulation = self.__get_initial_triangulation(convex_hull)
        rest_indices = [item for item in range(len(points)) if item not in convex_hull.vertices]
        return self.__calculate_complete_triangulation(initial_triangulation, points, rest_indices)
    def __calculate_convex_hull(self, points:list[Point]) -> ConvexHull:
        return ConvexHull(Point_list_to_npArray_converter().list_of_points_to_nparray(points))
    def __get_initial_triangulation(self, convex_hull: ConvexHull):
        result = [] 
        for i in range(1, len(convex_hull.vertices) - 1):
            result.append(Triangle(convex_hull.vertices[0], convex_hull.vertices[i], convex_hull.vertices[i+1]))
        return result
    def __calculate_complete_triangulation(self, triangulation, points, rest_indices) -> list[Triangle]:
        stack = rest_indices.copy()
        for index in rest_indices:
            effected_triangles = self.__get_list_of_efected_triangles(triangulation, points, points[index])
            triangulation = Triangulation_updater().change_triangulation_according_effected_triangles(effected_triangles, triangulation, index)
        return triangulation
    def __get_list_of_efected_triangles(self, triangles: list[Triangle], points: list[Point], point: Point) -> list[Triangle]:
        result = list[Triangle]()
        for triangle in triangles:
            is_point_inside = self.__is_point_inside_triangle(triangle, points, point)
            is_point_on_edge = self.__is_point_on_edge(triangle, points, point)
            if is_point_inside or is_point_on_edge:
                result.append(triangle)
        return result       
    def __is_point_inside_triangle(self, triangle:Triangle, points: list[Point], point:Point) -> bool:
        polygon = Polygon([(points[triangle.point_index1].x, points[triangle.point_index1].y), (points[triangle.point_index2].x, points[triangle.point_index2].y),
                           (points[triangle.point_index3].x, points[triangle.point_index3].y)])
        return PointShapely(point.x, point.y).within(polygon)
    def __is_point_on_edge(self, triangle:Triangle, points: list[Point], point:Point) -> bool:
        polygon = Polygon([(points[triangle.point_index1].x, points[triangle.point_index1].y), (points[triangle.point_index2].x, points[triangle.point_index2].y),
                           (points[triangle.point_index3].x, points[triangle.point_index3].y)])
        return PointShapely(point.x, point.y).distance(polygon) < 1e-15
        