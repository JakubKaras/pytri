import pygame as pg
import pygame_menu as pg_menu
import enum
import json
import path
from geometric_objects import Triangulation, Point, Triangle
from visualization import draw_triangles, draw_text
from triangulation_algorithms import AlgorithmEnum

def set_algorithm(algorithm_selection, selection_id):
    print(algorithm_selection, selection_id)

def main(window, config, algorithm_selection):
    window.fill(pg_menu.themes.THEME_BLUE.background_color)
    pg.display.set_caption("Delauney Triangulation")
    CLOCK = pg.time.Clock()
    triangulation = Triangulation([Point(500, 500), Point(400, 400), Point(300, 600), Point(800, 200)], [Triangle(0, 2, 3), Triangle(0, 1, 3)])

    run = True
    while run:
        CLOCK.tick(config['fps'])

        draw_triangles(window, triangulation)
        draw_text(window, "Press ESCAPE to return to menu", pg.font.SysFont(config['font']['name'], config['font']['size']), config['text_colour'], 375, 0)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    x, y = pg.mouse.get_pos()
                    triangulation.add_point(Point(x, y), algorithm_selection)
            if event.type == pg.QUIT or event.type == pg.KEYDOWN:
                run = False
                if event.type == pg.KEYDOWN and event.key != pg.K_ESCAPE:
                    run = True
                break


if __name__ == '__main__':
    with path.CONFIG.open() as f:
        config = json.load(f)
    pg.init()
    window = pg.display.set_mode((config['window']['width'], config['window']['height']))
    menu = pg_menu.Menu('Select the triangulation algorithm', config['window']['width'], config['window']['height'], theme=pg_menu.themes.THEME_BLUE)
    selection = menu.add.selector('Triangulation algorithm :', [(AlgorithmEnum.FLIPPING.value, AlgorithmEnum.FLIPPING), (AlgorithmEnum.INCREMENTAL.value, AlgorithmEnum.INCREMENTAL)])
    menu.add.button('Run', lambda: main(window, config, selection.get_value()[0][1]))
    menu.add.button('Quit', pg_menu.events.EXIT)
    menu.mainloop(window)