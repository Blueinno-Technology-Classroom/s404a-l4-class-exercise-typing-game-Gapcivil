import pgzrun
import random
from pgzhelper import *


WIDTH=1000
HEIGHT=800

zombie_run_img=['zombie/run/tile002','zombie/run/tile003','zombie/run/tile004','zombie/run/tile005']
zombie_die_img=['zombie/die/tile014','zombie/die/tile015','zombie/die/tile016','zombie/die/tile017','zombie/die/tile018','zombie/die/tile019','zombie/die/tile020','zombie/die/tile021','zombie/die/tile022','zombie/die/tile023','zombie/die/tile024',]
player_idle_img=['hero/idle/tile000','hero/idle/tile001','hero/idle/tile002','hero/idle/tile003','hero/idle/tile004','hero/idle/tile005','hero/idle/tile006','hero/idle/tile007',]
player_die_img=['hero/die/tile000','hero/die/tile001','hero/die/tile002','hero/die/tile003','hero/die/tile004','hero/die/tile005',]
player_attack_img=['hero/attack/tile000','hero/attack/tile001','hero/attack/tile002','hero/attack/tile003','hero/attack/tile004','hero/attack/tile005',]


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

fireball_img=['fireball/fireball1','fireball/fireball2','fireball/fireball3','fireball/fireball4','fireball/fireball5']
fireball=Actor(fireball_img[0])
fireball.fps=100
fireball.images=fireball_img
fireball.scale=4
fireball.active=False

word_list = ['James', 'Mary', 'Michael', 'Patricia', 'Robert', 'Jennifer', 'John', 'Linda', 'David', 'Elizabeth', 'William', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 'Thomas', 'Karen', 'Christopher', 'Sarah', 'Charles', 'Lisa', 'Daniel', 'Nancy', 'Matthew', 'Sandra', 'Anthony', 'Betty', 'Mark', 'Ashley', 'Donald', 'Emily', 'Steven', 'Kimberly', 'Andrew', 'Margaret', 'Paul', 'Donna', 'Joshua', 'Michelle', 'Kenneth', 'Carol', 'Kevin', 'Amanda', 'Brian', 'Melissa', 'Timothy', 'Deborah', 'Ronald', 'Stephanie', 'George', 'Rebecca', 'Jason', 'Sharon', 'Edward', 'Laura', 'Jeffrey', 'Cynthia', 'Ryan', 'Dorothy', 'Jacob', 'Amy', 'Nicholas', 'Kathleen', 'Gary', 'Angela', 'Eric', 'Shirley', 'Jonathan', 'Emma', 'Stephen', 'Brenda', 'Larry', 'Pamela', 'Justin', 'Nicole', 'Scott', 'Anna', 'Brandon', 'Samantha', 'Benjamin', 'Katherine', 'Samuel', 'Christine', 'Gregory', 'Debra', 'Alexander', 'Rachel', 'Patrick', 'Carolyn', 'Frank', 'Janet', 'Raymond', 'Maria', 'Jack', 'Olivia', 'Dennis',
             'Heather', 'Jerry', 'Helen', 'Tyler', 'Catherine', 'Aaron', 'Diane', 'Jose', 'Julie', 'Adam', 'Victoria', 'Nathan', 'Joyce', 'Henry', 'Lauren', 'Zachary', 'Kelly', 'Douglas', 'Christina', 'Peter', 'Ruth', 'Kyle', 'Joan', 'Noah', 'Virginia', 'Ethan', 'Judith', 'Jeremy', 'Evelyn', 'Christian', 'Hannah', 'Walter', 'Andrea', 'Keith', 'Megan', 'Austin', 'Cheryl', 'Roger', 'Jacqueline', 'Terry', 'Madison', 'Sean', 'Teresa', 'Gerald', 'Abigail', 'Carl', 'Sophia', 'Dylan', 'Martha', 'Harold', 'Sara', 'Jordan', 'Gloria', 'Jesse', 'Janice', 'Bryan', 'Kathryn', 'Lawrence', 'Ann', 'Arthur', 'Isabella', 'Gabriel', 'Judy', 'Bruce', 'Charlotte', 'Logan', 'Julia', 'Billy', 'Grace', 'Joe', 'Amber', 'Alan', 'Alice', 'Juan', 'Jean', 'Elijah', 'Denise', 'Willie', 'Frances', 'Albert', 'Danielle', 'Wayne', 'Marilyn', 'Randy', 'Natalie', 'Mason', 'Beverly', 'Vincent', 'Diana', 'Liam', 'Brittany', 'Roy', 'Theresa', 'Bobby', 'Kayla', 'Caleb', 'Alexis', 'Bradley', 'Doris', 'Russell', 'Lori', 'Lucas', 'Tiffany',]

question=random.choice(word_list).lower()
response=''





def update():
    global response
    global question
    zombie.animate()
    player.animate()
    fireball.animate()
    if not (player.image in player_die_img)and not (zombie.image in zombie_die_img):
        zombie.x-=3
    if player.image==player_die_img[-1]:
        player.images=player_idle_img
        player.fps=20
    if player.image==player_attack_img[-1]:
        player.images=player_idle_img
    if zombie.image==zombie_die_img[-1]: #-1 means last one of the list for zombie_die_img, aka zombie/die/tile024
        zombie.images=zombie_run_img
        zombie.right=WIDTH

    
    if zombie.left<=0:
        zombie.right=WIDTH+100
        response=''
    if zombie.collide_pixel(player) and not (player.image in player_attack_img):
        zombie.right=WIDTH+100
        response=''
        player.images=player_die_img
        player.fps=5
    if player.collide_pixel(zombie):
        zombie.right=WIDTH+100
        response=''
        player.images=player_attack_img
        player.fps=5
    if fireball.active:
        fireball.move_forward(5)
        if fireball.collide_pixel(zombie):
                fireball.active=False
                zombie.images=zombie_die_img


def on_key_down(key):
    global response
    global question
    if key in range(97,123):
        print(chr(key))
        response+=chr(key)
    elif key==32: #spacebar
        if response==question:
            print('correct')
            response=''
            question=random.choice(word_list).lower()
            player.images=player_attack_img
            fireball.y=player.y
            fireball.pos=player.pos
            fireball.active=True

    elif key==keys.BACKSPACE: #key 8
        response=response[0:-1]




def draw():
    screen.clear()
    zombie.draw()
    screen.draw.text(question,(50,100),fontsize=120)
    screen.draw.text(response,(50,100),fontsize=120,color='green')
    player.draw()
    if fireball.active:
        fireball.draw()

pgzrun.go()