
# importing all the libraries needed
import pygame
from pygame.transform import rotate,flip
from random import randint
import math
from pygame import mixer
import os

import tkinter as tk
from tkinter import *

# initialize the game
pygame.init()

# the domain you want the application to publish your score
yotam_domain = "yotam.store"

# images per level for the enemies
image_trucks = [['truck1.png','truck2.png','truck3.png','truck4.png','truck5.png'],
                ['shuriken1.png','shuriken2.png','shuriken3.png','shuriken4.png'],
                ['snake1.png','snake2.png','snake3.png','snake4.png'],
                ['alien1.png','alien2.png','alien3.png','alien4.png','alien5.png']]

# images per level for the player
image_player = ['car.png', 'ninja.png', 'mouse.png', 'rocket.png']

# images per level for the background
backgrounds = ['background1.jpg','background2.jpg','background3.jpg','background4.jpg']

# add nusic to the game
mixer.music.load("Queen - Don't Stop Me Now (Official Video).mp3")
mixer.music.set_volume(0.75)
mixer.music.play(-1)

# create level
level = 0

# create the score
score = 0
score_font = pygame.font.Font('Skygraze.otf', 30)

# level text
my_font = pygame.font.Font('Skygraze.otf', 40)
my_level_text = my_font.render(f"level {level+1}", True, (0, 0, 0))

# a variable to define how many levels do the game has.
# this variable is critical for check_status function to know when go to win_game function.
max_level = 3

# manage the car speed and the enemies speed
car_speed = 1.2
truck_speed_t = 0.2

# variable that manage that only one action will happen at a time
allow = True

# level to truck speed, to increase the enemy speed every level
def lev_to_truck_speed(level):
    global truck_speed
    match level:
        case 1:
            truck_speed = 0.25
        case 2:
            truck_speed = 0.3
        case 3:
            truck_speed = 0.35
        case default:
            truck_speed = 0.4

# creating the screen
screen = pygame.display.set_mode((832,640))
background = pygame.image.load("./images/backgrounds/"+backgrounds[level])

# creating title and icon
icon = pygame.image.load('./images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Crossy Road')

# create clock
clock = pygame.time.Clock

# create car variables
car_x = 320
car_y = 576
change_x = 0
change_y = 0
wanted_x = car_x
wanted_y = car_y
car_image = pygame.image.load("./images/character/"+image_player[level])

# function to make the player slide to the chosen direction
def slide(direction):

    global allow
    global car_x
    global car_y
    global change_x
    global change_y
    global wanted_x
    global wanted_y

    allow = False

    if direction == 'forward':
        wanted_y = car_y - 64
        change_y = -car_speed

    if direction == 'left':
        wanted_x = car_x - 64
        change_x = -car_speed

    if direction == 'right':
        wanted_x = car_x + 64
        change_x = car_speed


# to check if something unusual happened in the game
# and keep the player where he supposed to be...
# this function also know when it's needed to continue to the next level.
def check_status():
    global allow
    global car_x
    global car_y
    global change_x
    global change_y
    global wanted_x
    global wanted_y
    global is_running

    if car_x > wanted_x and change_x > 0:
        car_x = wanted_x
        allow = True
        change_x = 0
        change_y = 0

    if car_x < wanted_x and change_x < 0:
        car_x = wanted_x
        allow = True
        change_x = 0
        change_y = 0

    if car_y < wanted_y:
        car_y = wanted_y
        allow = True
        change_x = 0
        change_y = 0

    if car_x < 0:
        car_x = 0
        wanted_x = 0
        change_x = 0
        allow = True
    if car_x > 768:
        car_x = 768
        wanted_x = 768
        change_x = 0
        allow = True
    if car_y == 0:
        if level == max_level:
            game_over()
            is_running = False
        else:
            next_level()

# class to create a enemy whenever is needed
class Truck:
    def __init__(self, index, layer):
        # the constructor considers the layer to decide the direction of the enemy
        if layer%2 == 0:
            self.direction = 'right'
            self.truck_speed = truck_speed_t
            self.truck_x = index * 64
            self.truck_y = 640 - (64 * layer)
            images = image_trucks[level]
            self.image=pygame.image.load("./images/enemies/"+images[randint(0,len(images)-1)])
        else:
            self.direction = 'left'
            self.truck_speed = -1*truck_speed_t
            self.truck_x = index * 64
            self.truck_y = 640 - (64 * layer)
            images = image_trucks[level]
            self.image = flip(pygame.image.load("./images/enemies/"+images[randint(0, len(images)-1)]),True,False)

    def setX(self):
        self.truck_x += self.truck_speed
        if self.truck_x > 832:
            self.truck_x = -64
        if self.truck_x < -64:
            self.truck_x = 832

    # if the game is over, then all the enemies need to stop mooving
    def setXgameover(self):
        self.truck_speed = 0

    def getX(self):
        return self.truck_x
    def getY(self):
        return self.truck_y

    def rotateTruck(self):
        self.image = rotate(self.image,90)

    def printTruck(self):
        screen.blit(self.image, (self.truck_x,self.truck_y))

# variables to build a "matrix" of enemies
layers= [2,3,4,6,7,8,9]
indexes = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# list of all the enemies in the game
all_trucks = []

# building the enemies matrix for the first time
for l in layers:
    for i in indexes:
        # randomly create an enemy in the specified position
        if randint(0,1) == 1:
            new_truck = Truck(i,l)
            # adding the new enemy to the enemies list
            all_trucks.append(new_truck)

# function to decide if there is a collision between the player and an enemy
def isCollision(x1,y1,x2,y2):
    dis = math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
    if dis < 37:
        return True
    else:
        return False


# define function for level up
def next_level():
    global allow
    global car_x
    global car_y
    global change_x
    global change_y
    global wanted_x
    global wanted_y
    global level
    global truck_speed
    global background
    global car_image
    global  my_level_text

    level += 1
    my_level_text = my_font.render(f"level {level + 1}", True, (0, 0, 0))
    truck_speed = lev_to_truck_speed(level)
    background = pygame.image.load("./images/backgrounds/"+backgrounds[level])
    car_image = pygame.image.load("./images/character/"+image_player[level])

    # reset the player position
    car_x = 320
    car_y = 576
    change_x = 0
    change_y = 0
    wanted_x = car_x
    wanted_y = car_y

    # delete all the enemies
    all_trucks.clear()

    # creating new enemies
    for l in layers:
        for i in indexes:
            if randint(0, 1) == 1:
                new_truck = Truck(i, l)
                all_trucks.append(new_truck)

    allow = True


# game over
def game_over():    
    global first_window, f1_text, f2_text, yotam_domain
    first_window = tk.Tk()
    first_window.title("share your score")
    first_window.geometry("400x400")
    first_window.configure(bg="lightgreen")

    f1_text = tk.Entry(first_window)
    f1_text.insert(0, f"{yotam_domain}")
    f2_text = tk.Entry(first_window)
    f2_text.insert(1, 'username')
    f1_text.pack()
    f2_text.pack()
    
    first_button = Button(first_window, text="submit", bg="lightblue", command=curl_to_host)
    first_button.pack()
    first_window.mainloop()
    
    
def curl_to_host():
    global first_window, IP, username, score
    IP = f1_text.get()
    username = f2_text.get()
    print(IP, username, score)
    try:
        os.system(f"curl -X POST 'https://{IP}/add_score?user={username}&score={score}' --insecure")
    except:
        pass
    first_window.destroy()






# GAME LOOP
global is_running
is_running = True
while is_running:

    # show the screen
    screen.blit(background, (0,0))
    screen.blit(my_level_text,(300,10))
    score_text = score_font.render(f"SCORE: {score}", True, (255, 255, 255))
    screen.blit(score_text, (50, 590))


    for event in pygame.event.get():

        # auto close when quit
        if event.type == pygame.QUIT:
            is_running = False

        # define car movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and allow:
                slide('forward')
                score += 10
            if event.key == pygame.K_LEFT and allow:
                slide('left')
            if event.key == pygame.K_RIGHT and allow:
                slide('right')

    check_status()

    car_x += change_x
    car_y += change_y

    for n in all_trucks:
        # check for possible collisions
        if isCollision(n.getX(),n.getY(),car_x,car_y):
            is_running = False
            game_over()
        
        n.setX()

        # in specific level (second) the shurikan enemies need to rotate non-stop.
        if level == 1:
            n.rotateTruck()
        n.printTruck()
    screen.blit(car_image,(car_x,car_y))

    pygame.display.update()