from geometric_objects import Triangulation
from convex_hull_triangulation import Convex_hull_triangulation

class Flipping_delauney_algorithm:
    def calculate_triangulation(self, triangulation: Triangulation):
        triangulation.triangles = Convex_hull_triangulation().calculate_triangulation(triangulation.points)
        triangles = triangulation.triangles.copy()
        while len(triangles) > 0:
            triangulation.perform_circumcircle_check_for_all_vertices(triangles.pop(0))
        return triangulation.triangles



