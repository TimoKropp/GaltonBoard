import pygame
import random
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)

rad = 1             #radius for a ball
N_Balls = 5000      #number of balls
size = 300          #window size, width = size/2, hight = size
level = 500         #ground level to draw bars
width = 1           #width of a bar
clock_tick = 100    #clock tick, simulation speed

class Ball():
    def __init__(self, x, y, rad):    
        self.x = x
        self.y = y
        self.rad=rad

    def draw(self, screen):
        self.screen = screen
        #circle(surface, color, center, radius)
        pygame.draw.circle(self.screen, white, [self.x, self.y], self.rad)

    def move(self):   
        if self.y > 10 and self.y < level:        
            self.y += 1
            self.x += [-1,1][random.randrange(2)]
        else: 
            self.y += 1

class Bar():
    def __init__(self,level,width,pos,h):    
        self.level = level
        self.width = width
        self.pos = pos
        self.h = h
    def draw(self,screen):
        self.screen=screen
        pygame.draw.line(self.screen, white, [self.pos, self.level],[self.pos, self.level-self.h], self.width)


### Initializing ###
pygame.init()
w_h = [size,2*size]
screen = pygame.display.set_mode(w_h)
pygame.display.set_caption("Galton Animation")
stop = False
clock = pygame.time.Clock()
Balls = []
Bars=[]

## Create Balls ###
for k in range(0,N_Balls):
        x=int(size/2)
        y=1-(N_Balls-k)
        Balls.append(Ball(x,y,rad))

### create Bars ###        
for j in range(0,size):
    Bars.append(Bar(level,width,j,0))

#### Loop ####
while stop == False: # check for exit
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            stop = True # Flag that we are done so we exit this loop
            
    screen.fill(black)
    
    for b in range(0,N_Balls):
        Balls[b].draw(screen)
        Balls[b].move()
            
        if Balls[b].y == level:   
           Bars[Balls[b].x].h +=1

    for j in range(0,size):  
        Bars[j].draw(screen)
 
    clock.tick(clock_tick)
    pygame.display.flip()

pygame.quit()