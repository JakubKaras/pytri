import pygame as pg
from geometric_objects import Triangulation, Point

def draw_text(window, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))

def draw_points(window, points: list[Point], point_colour, point_radius):
    for point in points:
        pg.draw.circle(window, point_colour, point.to_tuple(), point_radius)

def draw_lines(window, points: list[Point], line_colour, line_width):
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            pg.draw.line(window, line_colour, points[i].to_tuple(), points[j].to_tuple(), line_width)

def draw_triangles(window, triangulation: Triangulation, point_colour = (90, 115, 230), point_radius = 5, line_colour = (100, 100, 90), line_width = 3):
    num_of_points = len(triangulation.points)
    for triangle in triangulation.triangles:
        draw_lines(window, [triangulation.points[i] for i in triangle.to_list() if i < num_of_points], line_colour, line_width)
    draw_points(window, triangulation.points, point_colour, point_radius)