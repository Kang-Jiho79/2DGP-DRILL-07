from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(0, 800), 90
        self.frame = random.randint(0, 7)
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

class SmallBall:
    def __init__(self):
        self.image = load_image("ball21x21.png")
        self.x, self.y = random.randint(0, 800), 599
        self.speed = random.randint(5, 10)
    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()


def reset_world():
    global running
    global world
    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for _ in range(11)]
    world += team

    balls = [SmallBall() for _ in range(10)]
    pass

def update_world():
    for o in world:
        o.update()
    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()
    pass


reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
