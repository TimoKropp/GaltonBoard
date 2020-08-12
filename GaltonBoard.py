import pygame
import random
import os

# simulation settings
rad         =  1            # radius of a Ball
N_Balls     = 3000          # number of Balls
size        = 300           # window size, width = size/2, height = size
width       = 2             # width of a bar
clock_tick  = 100           # clock tick, simulation speed
level_red   = 300           # level to trap and count Balls in red (y-position in window)
level_blue  = 500           # level to trap and count Balls in blue (y-position in window)
final_level = level_blue    # end of Galton Board

# Define some colors for drawing
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)

class Ball():
    def __init__(self, x, y, rad):    
        self.x   = x
        self.y   = y
        self.rad = rad

    def draw(self, screen):
        self.screen = screen
        #circle(surface, color, center, radius)
        pygame.draw.circle(self.screen, white, [self.x, self.y], self.rad)

    def move(self):
        if self.y > 10 and self.y < final_level:    # check if inside Galton Board (starts at 10, ends at final_level)
            self.y += 1                             # move 1 step in y direction
            self.x += [-1,1][random.randrange(2)]   # move 1 step randomly in x direction, left or right
        else: 
            self.y += 1                             # move 1 step in y direction if outside the Galton Board

class Bar():
    def __init__(self, level, width, pos, height, color):
        self.level  = level
        self.width  = width
        self.pos    = pos
        self.height = height
        self.color  = color

    def draw(self, screen):
        self.screen = screen
        pygame.draw.line(self.screen, self.color, [self.pos, self.level],[self.pos, self.level-self.height], self.width)



# Initializing 
Balls = []
BarsRed = []
BarsBlue = []

pygame.display.init()
w_h = [size, 2 * size] # aspect ration: height = 2 * width
screen = pygame.display.set_mode(w_h)
pygame.display.set_caption("Galton Animation")
stop = False
clock = pygame.time.Clock()

# create Balls
for k in range(0, N_Balls):
    x = int( size / 2)
    y = 1 - (N_Balls - k)
    Balls.append(Ball( x, y, rad))

# create Bars       
for j in range(0, size):
    BarsRed.append(Bar(level_red, width, j, 0,  red))   # init Bars with 0 height: creates horizontal line at level_red
    BarsBlue.append(Bar(level_blue, width, j, 0, blue)) # init Bars with 0 height: creates horizontal line at level_blue

# Loop 
while stop == False:                    # check for exit
    for event in pygame.event.get():    # User did something
        if event.type == pygame.QUIT:   # If user clicked close
            stop = True                 # Flag that we are done so we exit this loop
            
    screen.fill(black)
    
    for b in range(0, N_Balls):              # draw and move every Ball
        Balls[b].draw(screen)
        Balls[b].move()
            
        if Balls[b].y == level_red:         # if Ball reaches level (y-position in window)
           BarsRed[Balls[b].x].height += 1  # increase Bar height by 1 on the same x position

        if Balls[b].y == level_blue:
           BarsBlue[Balls[b].x].height += 1

    for j in range(0,size):                 # draw all Bars
        BarsRed[j].draw(screen)
        BarsBlue[j].draw(screen)

    clock.tick(clock_tick)
    pygame.display.flip()
    
pygame.display.quit()
