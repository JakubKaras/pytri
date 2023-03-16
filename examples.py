import logging
from data_classes import Triangulation, Point, Triangle, points_to_numpy_array

logger = logging.getLogger(__name__)
logging.basicConfig(format = '\n%(asctime)s %(module)s %(levelname)s: %(message)s', datefmt = '%I:%M:%S %p', level = logging.INFO)

def basic_triangulation_dataclass_example():
    points = [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)]
    point_triplets = [Triangle(0, 1, 2), Triangle(1, 2, 3)]
    triangulation = Triangulation(points=points, point_triplets=point_triplets)
    logging.getLogger().info(f"Points:\n{triangulation.points}")
    logging.getLogger().info(f"Points as numpy array:\n{points_to_numpy_array(triangulation.points)}")
    logging.getLogger().info(f"Point triplets:\n{triangulation.point_triplets}")

if __name__ == '__main__':
    basic_triangulation_dataclass_example()