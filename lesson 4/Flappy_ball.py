import pgzrun
import random

GRAVITY=2000.0
WIDTH=500
HEIGHT=2000
TITLE="Flappy bird"
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
colour=(r,g,b)

class Ball():
    def __init__(self,initial_x, initial_y):
        self.x=initial_x
        self.y=initial_y
        self.vx=200
        self.vy=0
        self.radius=40
    def draw_circle(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,colour)
ball=Ball(50,50)
def draw():
    screen.clear()
    screen.fill("red")
    ball.draw_circle()
def update(dt):
    uy=ball.vy
    ball.vy = ball.vy + (GRAVITY*dt)
    ball.y += (uy + ball.vy) * 0.5 * dt
    if ball.y > HEIGHT:
        ball.y=HEIGHT - ball.radius
        #inelastic collision
        ball.vy =- ball.vy * 0.9
    ball.x+=ball.vx*dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx
def on_key_down(key):
    if key == keys.UP:
        ball.vy = -500
pgzrun.go()