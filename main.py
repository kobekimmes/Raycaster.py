import pygame as pg
import sys
from map import *
from camera import *
from raycasting import *


class Game:

    def __init__(self, res, FPS):
        pg.init()
        self.running = True
        self.res = res
        self.FPS = FPS
        self.screen = pg.display.set_mode((res * 20, res * 20))
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.newGame()

    def newGame(self):
        self.map = Map(self)
        self.camera = Camera(self, 300, 300)
        self.ray = Raycast(self)

    def update(self):
        self.camera.update()
        self.ray.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(self.FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def showGrid(self):
        for i in range(20):
            pg.draw.line(self.screen, "white", (i * self.res, 0), (i * self.res, i * self.res * 20))
        for i in range(20):
            pg.draw.line(self.screen, "white", (0, i * self.res), (i * self.res, i * self.res * 20))

    def draw(self):
        self.screen.fill("black")
        self.showGrid()
        self.map.draw()
        self.camera.draw()

    def run(self):
        while self.running:
            self.draw()
            self.checkEvents()
            self.update()
        pg.quit()


game = Game(40, 60)
game.run()