import pgzrun
import random
WIDTH=600
HEIGHT=400
sat=[]
for i in range(10):
    s=Actor("satellite")
    s.x=random.randint(0,550)
    s.y=random.randint(0,350)
    sat.append(s)
def draw():
    screen.blit("background",(0,0))
    for s in sat:
        s.draw()
pgzrun.go()