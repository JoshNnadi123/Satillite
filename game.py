import pgzrun
import random
from time import time
WIDTH=600
HEIGHT=400
next=0
lines=[]
sat=[]
start=time()
for i in range(10):
    s=Actor("satellite")
    s.x=random.randint(0,550)
    s.y=random.randint(0,350)
    sat.append(s)
def draw():
    number=1
    screen.blit("background",(0,0))
    global total
    for s in sat:
        s.draw()
        screen.draw.text(str(number),(s.x,s.y-25))
        number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,0,0))
    if next < 10:
        total=time()-start
        screen.draw.text(str(round(total,1)),(10,10))
    else:
        screen.draw.text(str(round(total,1)),(10,10))
def on_mouse_down(pos):
    global next
    global lines,sat
    if sat[next].collidepoint(pos):
        if next>0:
            lines.append((sat[next-1].pos,sat[next].pos))
        next=next+1
    else:
        lines=[]
        next=0
def update():
    pass
pgzrun.go()