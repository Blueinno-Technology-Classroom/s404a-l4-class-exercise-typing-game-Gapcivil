import pgzrun
from pgzhelper import *

WIDTH=1000
HEIGHT=800

zombie_run_img=['zombie/run/tile002','zombie/run/tile003','zombie/run/tile004','zombie/run/tile005']
player_idle_img=['hero/idle/tile000','hero/idle/tile001','hero/idle/tile002','hero/idle/tile003','hero/idle/tile004','hero/idle/tile005','hero/idle/tile006','hero/idle/tile007',]
player_die_img=['hero/die/tile000','hero/die/tile001','hero/die/tile002','hero/die/tile003','hero/die/tile004','hero/die/tile005',]
#player_attack_img=['hero/attack/tile000','hero/attack/tile001','hero/attack/tile002','hero/attack/tile003','hero/attack/tile004','hero/attack/tile005',]
zombie=Actor(zombie_run_img[0])
player=Actor(player_idle_img[0])
zombie.images=zombie_run_img
zombie.scale=5
zombie.fps=10
zombie.right=WIDTH+100
zombie.bottom=HEIGHT
player.images = player_idle_img
player.scale=5
player.fps=20
player.bottom=HEIGHT+390

question='hello world'
response=''




def update():
    global response
    zombie.animate()
    player.animate()
    if not (player.image in player_die_img):
        zombie.x-=3
    if player.image==player_die_img[-1]:
        player.images=player_idle_img
        player.fps=20
    if zombie.left<=0:
        zombie.right=WIDTH+100
        response=''
    if zombie.collide_pixel(player):
        zombie.right=WIDTH+100
        response=''
        player.images=player_die_img
        player.fps=5


def on_key_down(key):
    global response
    if key in range(97,123):
        print(chr(key))
        response+=chr(key)
    elif key==32: #spacebar
        response+=' '
    
    elif key==keys.BACKSPACE: #key 8
        response=response[0:-1]


def draw():
    screen.clear()
    zombie.draw()
    screen.draw.text(question,(50,100),fontsize=120)
    screen.draw.text(response,(50,100),fontsize=120,color='green')
    player.draw()

pgzrun.go()