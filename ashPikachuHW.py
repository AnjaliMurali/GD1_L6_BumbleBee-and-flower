import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

Ash = Actor("ash")
Ash.pos = 100,100

pikachu = Actor("pikachu")
pikachu.pos = 200,200

def draw():
    screen.blit("background", (0,0))
    pikachu.draw()
    Ash.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))

    if game_over:
            screen.fill("pink")
            screen.draw.text("Time's Up! Your Final Score: " + str(score), midtop=(WIDTH/2,10), 
            fontsize=40, color="red")


def place_flower():
    pikachu.x = randint(70, (WIDTH-70))
    pikachu.y = randint(70, (HEIGHT-70))


def time_up():
    global game_over 
    game_over = True

def update():
    global score
    # if keyboard.w:(for w key press)
    if keyboard.left:  
        Ash.x = Ash.x - 2
    if keyboard.right:
        Ash.x = Ash.x + 2
    if keyboard.up:
        Ash.y = Ash.y - 2
    if keyboard.down:
        Ash.y = Ash.y + 2

    flower_collected = Ash.colliderect(pikachu)

    if flower_collected:
        score = score + 10
        place_flower()


clock.schedule(time_up, 60.0)



pgzrun.go()

