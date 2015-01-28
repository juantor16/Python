
#import a library of functions called 'pygame'
import pygame
#intialize the game engine
pygame.init()
pygame.font.init()

#defining colors
black = (   0,   0,   0)
white = (255,255,255)
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
    ''' ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT'''
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    ''' ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT'''
  
  
    ''' ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT'''
 
    ''' ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT'''
 
     
    ''' ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT'''
    
    # clear the screen and set the screen background
    screen.fill(green)

    #Draw on the screen a green line from(0,0) to (100,100)
    #That is 5 pixels wide
    pygame.draw.line(screen,white,[0,0],[100,100],25)
    pygame.draw.line (screen,red, [0,0], [50,50],19)
    # Drawing a series of lines
    # draw on the screen several green lines from(0,10) to (100,110)
    #5 pixels wide using a while loop
    y_offset=0
    x_offset=0
    while y_offset < 100:
        pygame.draw.line(screen,black,[0,10+y_offset],[100,110+y_offset],13)
        y_offset=y_offset+10
    # using a for loop
    for y_offset in range(0,100,10):
        pygame.draw.line(screen,red,[0,10+y_offset],[100,11-+y_offset],5)

    #flipping the Pygame display
    pygame.display.flip()

    ''' ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT'''
      
    # Limit to 20 frames per second
    clock.tick(20)
#proper Shutdown of a Pygame program
pygame.quit()
