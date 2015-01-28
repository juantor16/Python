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



#Loop until the user clicks the close button.
done=False
  
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
  
# -------- Main Program Loop -----------
while done==False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
  
  
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
     
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
      
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
      
    # Limit to 20 frames per second
    clock.tick(20)  
#proper shutdown of a pygame program
pygame.quit()
