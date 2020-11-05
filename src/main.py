import sys
import objects
import pygame as pg
import random
from pygame.locals import QUIT

def initialize(num_ant, *args):
    '''
    num_ant: int
    args: pg.sprite.Group[]
    '''
    nest_x, nest_y = random.randrange(0, objects.world_size), random.randrange(0, objects.world_size)
    for i in range(num_ant):
        args[0].add(objects.Ant((nest_x, nest_y), "finding"))
    args[1].add(objects.Food((random.randrange(0, objects.world_size), random.randrange(0, objects.world_size)), 50))
    args[2].add(objects.Nest((nest_x, nest_y), 50))

def draw_pheromone(pheromone, surface):
    table = pheromone.table
    for i in range(objects.world_size):
        for j in range(objects.world_size):
            if table[i][j] != 0:
                sub_surf = pg.Surface(pg.Rect(i, j, 100, 100).size, pg.SRCALPHA)
                pg.draw.rect(sub_surf, (0, 255, 0, 100), sub_surf.get_rect())
                surface.blit(sub_surf, (i, j, 100, 100))

pg.init()
start = True
surface = pg.display.set_mode((objects.world_size, objects.world_size))
pg.display.set_caption('ACO Simulator')
background = objects.image.bkg
background.convert()
surface.blit(background, (0, 0))
pg.display.update()


ants = pg.sprite.Group()
foods = pg.sprite.Group()
nests = pg.sprite.Group()
pheromone = objects.Pheromone()
initialize(objects.num_ants, ants, foods, nests)
foods.draw(surface)
ants.draw(surface)
nests.draw(surface)
pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN: #press blankspace to start/pause
            if event.key == pg.K_SPACE:
                 start = not start
    if start:
        surface.blit(background, (0, 0))
        ants.update(foods)
        ants.clear(surface, background)
        draw_pheromone(pheromone, surface)
        foods.draw(surface)
        ants.draw(surface)
        nests.draw(surface)
        pg.display.update()
        pg.time.wait(objects.wait)
