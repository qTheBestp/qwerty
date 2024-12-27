import random
import time
import pygame as pg
scr = pg.display.set_mode((800, 600))
x = 380
y = 280
xsp = 20
ysp = 0
xt = [340, 360]
yt = [280, 280]
lenght = 2

xapple = random.randint(0, 780)//20*20
yapple = random.randint(0, 580)//20*20

while True:
    pg.display.flip()
    scr.fill((0, 255, 0))
    pg.draw.circle(scr, (255, 0, 0), (xapple, yapple), 10)
    pg.draw.circle(scr, (0, 0, 255), (x, y), 12.5)

    for i in range(-1, -lenght-1, -1):
        pg.draw.circle(scr, (0, 0, 255), (xt[i], yt[i]), 12.5)
        pg.draw.circle(scr, (0, 0, 255), (xt[i], yt[i]), 12.5)
    xt.append(x)
    yt.append(y)

    if xapple == x and yapple == y:
        xapple = random.randint(0, 780) // 20 * 20
        yapple = random.randint(0, 580) // 20 * 20
        lenght +=1
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                xsp = -20
                ysp = 0
            if i.key == pg.K_RIGHT:
                xsp = 20
                ysp = 0
            if i.key == pg.K_UP:
                xsp = 0
                ysp = -20
            if i.key == pg.K_DOWN:
                xsp = 0
                ysp = 20
    x += xsp
    y += ysp
    time.sleep(0.2)
    if x > 780:
        x = 0

    if x < 0:
        x = 780

    if y < 0:
        y = 580

    if y > 580:
        y = 0

    for i in range(-1, -lenght-1, -1):
        for j in range(-1, -lenght-1, -1):
            if x == xt[i] and y == yt[j]:
                while True:
                    scr.fill((255, 0, 0))
                    pg.display.flip()