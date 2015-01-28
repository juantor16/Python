#import a library of functions called 'pygame'
import pygame
#intialize the game engine
pygame.init()
pygame.font.init()

#defining colors
black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red   = ( 255,   0,   0)


#white on hexadecimal
white=[0xFF, 0xFF, 0xFF]

pi=3.141592653

# Set the width and height of the screen
size=[700,500]
screen=pygame.display.set_mode(size)

#setting the window title
pygame.display.set_caption("professor Craven's Cool Game")
