from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass

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

    pass

def update_world():
    pass


def render_world():
    pass


reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
