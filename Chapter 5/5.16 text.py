# When specifying a rectangle the computer needs a list of these four numbers in the order of (x,y,width,height).
# Draw a rectangle: pygame.draw.rect(screen,black,[20,20,250,100],2)

# Draw an ellipse. using a rectangle as the outside boundaries: pygame.draw.ellipse(screen,black,[20,20,250,100],2)

#Drawing an arc.
'''
# Draw an arc as part of an ellipse. Use radians to determine what
# angle to draw.
pygame.draw.arc(screen,green,[100,100,250,200],  pi/2,     pi, 2)
pygame.draw.arc(screen,black,[100,100,250,200],     0,   pi/2, 2)
pygame.draw.arc(screen,red,  [100,100,250,200],3*pi/2,   2*pi, 2)
pygame.draw.arc(screen,blue, [100,100,250,200],    pi, 3*pi/2, 2)
'''

# This draws a triangle using the polygon command
# pygame.draw.polygon(screen,black,[[100,100],[0,200],[200,200]],5)

#Drawing text on the screen
'''
# Select the font to use. Default font, 25 pt size.
font = pygame.font.Font(None, 25)
 
# Render the text. "True" means anti-aliased text. 
# Black is the color. The variable black was defined
# above as a list of [0,0,0]
# Note: This line creates an image of the letters, 
# but does not put it on the screen yet.
text = font.render("My text",True,black)
 
# Put the image of the text on the screen at 250x250
screen.blit(text, [250,250])'''

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
blue  = (0,0,128,0)
yellow= (255,255,0,0)

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

    # Drawing a rectangle
    pygame.draw.rect(screen,black,[150,150,250,100],25)

    # Drawing an ellipse
    pygame.draw.ellipse(screen,red,[163,163,225,75],)
    #Drawing an arc
    # Draw an arc as part of an ellipse. Use radians to determine what
    # angle to draw.
    pygame.draw.arc(screen,green,[162,162,224,75],  pi/2,     pi, 2)
    pygame.draw.arc(screen,black,[164,164,224,75],     0,   pi/2, 2)
    pygame.draw.arc(screen,white,[164,164,224,75],3*pi/2,   2*pi, 2)
    pygame.draw.arc(screen,blue, [164,164,224,75],    pi, 3*pi/2, 2)
    #Draw a polygon
    pygame.draw.polygon(screen,white,[[240,240],[164,164],[82,240]],5)
    pygame.draw.polygon(screen,white,[[240,480],[275,375],[164,480]],5)
    # Select the font to use. Default font, 25 pt size.
    font = pygame.font.Font(None, 50)
 
    # Render the text. "True" means anti-aliased text. 
    # Black is the color. The variable black was defined
    # above as a list of [0,0,0]
    # Note: This line creates an image of the letters, 
    # but does not put it on the screen yet.
    text=font.render("THIS IS MY SHIT!",True,yellow)
 
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [350,350])

    #Print text:
    
    
    #flipping the Pygame display
    pygame.display.flip()

    ''' ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT'''
      
    # Limit to 20 frames per second
    clock.tick(20)
#proper Shutdown of a Pygame program
pygame.quit()
