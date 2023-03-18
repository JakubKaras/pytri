import pygame as pg
import pygame_menu as pg_menu
import enum
from geometric_objects import Triangulation, Point, Triangle
from visualization import draw_triangles, draw_text

class AlgorithmEnum(enum.Enum):
    FLIPPING = 0
    INCREMENTAL = 1

def set_algorithm(algorithm_selection, selection_id):
    print(algorithm_selection, selection_id)

def main(window, algorithm_selection):
    window.fill(pg_menu.themes.THEME_BLUE.background_color)
    pg.display.set_caption("Delauney Triangulation")
    CLOCK = pg.time.Clock()
    triangulation = Triangulation([Point(500, 500), Point(400, 400), Point(300, 600), Point(800, 200)], [Triangle(0, 2, 3), Triangle(0, 1, 3)])

    run = True
    while run:
        CLOCK.tick(60)

        draw_triangles(window, triangulation)
        draw_text(window, "Press ESCAPE to return to menu", pg.font.SysFont('arial', 20), (150, 150, 150), 375, 0)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    pass
            if event.type == pg.QUIT or event.type == pg.KEYDOWN:
                run = False
                if event.type == pg.KEYDOWN and event.key != pg.K_ESCAPE:
                    run = True
                break


if __name__ == '__main__':
    pg.init()
    WINDOW = pg.display.set_mode((1000, 800))

    menu = pg_menu.Menu('Select the triangulation algorithm', 1000, 800, theme=pg_menu.themes.THEME_BLUE)
    selection = menu.add.selector('Triangulation algorithm :', [('Flipping', AlgorithmEnum.FLIPPING), ('Incremental', AlgorithmEnum.INCREMENTAL)])
    menu.add.button('Run', lambda: main(WINDOW, selection.get_value()[0]))
    menu.add.button('Quit', pg_menu.events.EXIT)
    menu.mainloop(WINDOW)