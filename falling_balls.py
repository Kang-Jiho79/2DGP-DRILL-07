from pico2d import *
import random


# Game object class here
class Grass:
    # 생성자 함수 초기화수행
    def __init__(self):
        # grass 객체의 속성을 정의하고 초기화
        self.image = load_image("grass.png")

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.image = load_image("run_animation.png")
        self.x = random.randint(100, 800)
        self.frame = random.randint(0, 7)

    def draw(self):
        self.image.clip_draw(self.frame * 100,0,100,100,self.x,90)

    def update(self):
        self.x += 5
        self.frame = (self.frame +1) % 8


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False





def reset_world():
    global running
    global world # world list - 모든 객체들을 갖고있는 list

    world = [] # 하나도 객체가 없는 월드
    running = True

    grass = Grass()
    world.append(grass)

    team = [Boy() for _ in range(11)]
    world += team

    pass

def update_world():
    for game_object in world:
        game_object.update()
    pass


def render_world():
    # 월드에 객체들을 그린다.
    clear_canvas()

    for game_object in world:
        game_object.draw()

    update_canvas()
    pass


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code
close_canvas()
