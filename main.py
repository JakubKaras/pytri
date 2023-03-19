import pygame as pg
import pygame_menu as pg_menu
import logging
import json
import path
from geometric_objects import Triangulation, Point, Triangle
from triangulation_algorithms import AlgorithmEnum, add_point_to_triangulation
from visualization import draw_triangles, draw_text

def main(window, config, algorithm_selection):
    pg.display.set_caption("Delauney Triangulation")
    CLOCK = pg.time.Clock()
    if config['use_dummy_initial_triangulation']:
        triangulation = Triangulation([Point(500, 500), Point(400, 400), Point(300, 600), Point(800, 200)], [Triangle(0, 2, 3), Triangle(0, 1, 3)])
    else:
        triangulation = Triangulation([], [])

    run = True
    while run:
        CLOCK.tick(config['fps'])
        window.fill(pg_menu.themes.THEME_BLUE.background_color)
        draw_triangles(window, triangulation)
        draw_text(window, "Press ESCAPE to return to menu", pg.font.SysFont(config['font']['name'], config['font']['size']), config['text_colour'], 375, 0)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    x, y = pg.mouse.get_pos()
                    triangulation = add_point_to_triangulation(triangulation, Point(x, y), algorithm_selection)
            if event.type == pg.QUIT or event.type == pg.KEYDOWN:
                run = False
                if event.type == pg.KEYDOWN and event.key != pg.K_ESCAPE:
                    run = True
                break


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(format = '\n%(asctime)s %(module)s %(levelname)s: %(message)s', datefmt = '%I:%M:%S %p', level = logging.INFO)

    with path.CONFIG.open() as f:
        config = json.load(f)
    pg.init()
    window = pg.display.set_mode((config['window']['width'], config['window']['height']))
    menu = pg_menu.Menu('Select the triangulation algorithm', config['window']['width'], config['window']['height'], theme=pg_menu.themes.THEME_BLUE)
    selection = menu.add.selector('Triangulation algorithm :', [(AlgorithmEnum.FLIPPING.value, AlgorithmEnum.FLIPPING), (AlgorithmEnum.INCREMENTAL.value, AlgorithmEnum.INCREMENTAL)])
    menu.add.button('Run', lambda: main(window, config, selection.get_value()[0][1]))
    menu.add.button('Quit', pg_menu.events.EXIT)
    menu.mainloop(window)