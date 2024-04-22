from tkinter import *
import random

#constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUD_COLOR = "#000000"


#definitions

class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

#score window
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="score:{}".format(score), font=('consolas', 40))
label.pack()


canvas = Canvas(window, bg=BACKGROUD_COLOR, height=GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_width()
screen_height = window.winfo_height()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (screen_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop() 




