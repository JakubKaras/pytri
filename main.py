import pygame as pg
from geometric_objects import Triangulation, Point, Triangle
from visualization import draw_triangles

if __name__ == '__main__':
    WINDOW = pg.display.set_mode((1000, 800))
    WINDOW.fill((255, 255, 255))
    pg.display.set_caption("Delauney Triangulation")
    CLOCK = pg.time.Clock()
    triangulation = Triangulation([Point(500, 500), Point(400, 400), Point(300, 600), Point(800, 200)], [Triangle(0, 2, 3), Triangle(0, 1, 3)])

    run = True
    while run:
        CLOCK.tick(10)

        draw_triangles(WINDOW, triangulation)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break