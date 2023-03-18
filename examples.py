import logging
from geometric_objects import Triangulation, Point, Triangle, points_to_numpy_array
from triangulation_algorithms import is_point_in_circumcircle, is_point_in_triangle

logger = logging.getLogger(__name__)
logging.basicConfig(format = '\n%(asctime)s %(module)s %(levelname)s: %(message)s', datefmt = '%I:%M:%S %p', level = logging.INFO)

def basic_triangulation_dataclass_example():
    points = [Point(0, 0), Point(1, 2), Point(1, 0), Point(2, 2)]
    point_triplets = [Triangle(0, 1, 2), Triangle(1, 2, 3)]
    triangulation = Triangulation(points=points, point_triplets=point_triplets)
    logging.getLogger().info(f"Points:\n{triangulation.points}")
    logging.getLogger().info(f"Points as numpy array:\n{points_to_numpy_array(triangulation.points)}")
    logging.getLogger().info(f"Point triplets:\n{triangulation.point_triplets}")

if __name__ == '__main__':
    # basic_triangulation_dataclass_example()
    print(is_point_in_circumcircle([Point(1, 1), Point(2, 3), Point(3, 1)], Point(2, 2)))
    print(is_point_in_triangle([Point(1, 1), Point(3, 1), Point(2, 3)], Point(2, 2)))