import enum
import logging


class AlgorithmEnum(enum.Enum):
    FLIPPING = 'Flipping'
    INCREMENTAL = 'Incremental'


def incremental_delauney_algorithm(triangulation):
    logging.getLogger().info("Incremental triangulation algorithm is not implemented yet.")
    return triangulation.point_triplets

def flipping_delauney_algorithm(triangulation):
    logging.getLogger().info("Flipping triangulation algorithm is not implemented yet.")
    return triangulation.point_triplets