import unittest as ut
import numpy as np
from geometric_objects import Point, Triangle, points_to_numpy_array


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