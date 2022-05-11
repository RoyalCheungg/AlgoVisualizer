# import libraries 
import pygame 
import random 

# intialize constructor 
pygame.init() 

class globalValues:

    # creating our colors 
    colBlack = 0, 0, 0
    colWhite = 255, 255, 255
    colGreen = 0, 255, 0 
    colRed = 255, 0, 0
    colGrey = 128, 128, 128
    background_Col = colWhite

    side_pad = 100 
    top_pad = 150

    # define frame of the visualizer 

    def __init__(self, width, height, lst): 
        self.width = width 
        self.height = height

        # creating a GUI with width and height as parameters 
        self.window = pygame.display.set_mode((width, height)) 
        pygame.display.set_caption("Sorting Algorithm Algorithm Visualizer") 

        self.set_list(lst) 

        def set_list(self, lst):
            self.lst = lst 
            self.min_val = min(lst)
            self.max_val = max(lst) 
        
            # assigning the total area of each bar
            self.bar_width = round(self.width - self.side_pad / len(lst)) 
            self.bar_height = round((self.height - self.top_pad) / (self.max_val - self.min))
            self.x_start = self.side_pad // 2   

# creating starting list function for our program 

def generate_start_list(n, min_val, max_val): 
    lst = [] 
    # do this n number of times 
    for _ in range(n): 
        val = random(randint(min_val, max_val) 
        lst.append(val) 

    # the new list is now generated 
    return lst  

# this is our main function to show what we have currently 
def main(): 

    run = True 
    clock = pygame.clock() 
    # in pygame, must have a constant loop running 
    # for example, if you draw something on screen, program will draw and then immediately end
    # we do not want this, we want it to continously run UNTIL we end it manually   
    
    while run:  
        clock.tick(60) 
