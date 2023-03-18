import unittest as ut
import numpy as np
from geometric_objects import Point, Triangle, Triangulation, points_to_numpy_array, distance_point_to_point


class TestPointClass(ut.TestCase):
    def setUp(self) -> None:
        self.point1 = Point(1, 2)
        self.point2 = Point(1, 2)
        self.point3 = Point(2, 2)
        self.point4 = Point(1, 3)
        self.point5 = Point(4, 5)
        self.point_list = [self.point1, self.point2, self.point3, self.point4, self.point5]

    def test_that_the_same_instances_are_the_same(self):
        self.assertEqual(self.point1, self.point1)

    def test_that_objects_with_same_values_are_the_same(self):
        self.assertEqual(self.point1, self.point2)

    def test_that_objects_different_first_values_are_different(self):
        self.assertNotEqual(self.point1, self.point3)

    def test_that_objects_different_second_values_are_different(self):
        self.assertNotEqual(self.point1, self.point4)

    def test_that_objects_different_values_are_different(self):
        self.assertNotEqual(self.point1, self.point5)

    def test_tuple_conversion(self):
        self.assertEqual(self.point1.to_tuple(), (self.point1.x, self.point1.y))

    def test_numpy_array_conversion_shape(self):
        self.assertEqual(points_to_numpy_array(self.point_list).shape, (len(self.point_list), 2))

    def test_numpy_array_conversion_first_coordinates_are_same(self):
        self.assertTrue(np.all(points_to_numpy_array(self.point_list)[:, 0] == np.array([point.x for point in self.point_list])))

    def test_numpy_array_conversion_second_coordinates_are_same(self):
        self.assertTrue(np.all(points_to_numpy_array(self.point_list)[:, 1] == np.array([point.y for point in self.point_list])))


class TestTriangleClass(ut.TestCase):
    def test_list_conversion(self):
        triangle = Triangle(0, 2, 1)
        self.assertEqual(triangle.to_list(), [triangle.point_index1, triangle.point_index2, triangle.point_index3])

class TestDistances(ut.TestCase):
    def setUp(self) -> None:
        self.point1 = Point(0, 0)
        self.point2 = Point(1, 2)
        self.point3 = Point(1, 0)
        self.point4 = Point(2, 2)
        self.triangulation = Triangulation([self.point1, self.point2, self.point3, self.point4], [])
        self.outside_point = Point(3, 3)

    def test_that_distance_point_to_itself_is_zero(self):
        for point in self.triangulation.points:
            self.assertEqual(distance_point_to_point(point, point), 0)

    def test_symmetry_of_point_to_point_distance(self):
        for i in range(len(self.triangulation.points) - 1):
            for j in range(i + 1, len(self.triangulation.points)):
                self.assertEqual(
                    distance_point_to_point(self.triangulation.points[i], self.triangulation.points[j]),
                    distance_point_to_point(self.triangulation.points[j], self.triangulation.points[i])
                )

    def test_triangle_inequality_of_point_to_point_distance(self):
        for i in range(len(self.triangulation.points) - 2):
            for j in range(i + 1, len(self.triangulation.points) - 1):
                for k in range(j + 1, len(self.triangulation.points)):
                    i_to_j_distance = distance_point_to_point(self.triangulation.points[i], self.triangulation.points[j])
                    j_to_k_distance = distance_point_to_point(self.triangulation.points[j], self.triangulation.points[k])
                    i_to_k_distance = distance_point_to_point(self.triangulation.points[i], self.triangulation.points[k])
                    self.assertGreaterEqual(i_to_j_distance + j_to_k_distance, i_to_k_distance)

    def test_distance_of_triangulations_point_to_the_triangulation_is_zero(self):
        for point in self.triangulation.points:
            self.assertEqual(self.triangulation.distance_point_to_triangulation(point), 0)

    def test_distance_to_concrete_point(self):
        self.assertEqual(self.triangulation.distance_point_to_triangulation(self.outside_point), np.sqrt(2))