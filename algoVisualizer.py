# import libraries 

import math
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
    background_Col = colWhite
    
    gradient_Col = [ 
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ] 

    side_pad = 200 
    top_pad = 250

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
        self.bar_width = round((self.width - self.side_pad) / len(lst)) 
        self.bar_height = round((self.height - self.top_pad) / (self.max_val - self.min_val))
        self.start_x = self.side_pad // 2   

def draw(draw_info):
    draw_info.window.fill(globalValues.background_Col)
    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info):
    lst = draw_info.lst 
    for i, val in enumerate(lst): 
        x = draw_info.start_x + i * draw_info.bar_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.bar_height

        color = draw_info.gradient_Col[i % 3] # this will have a different element color 

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.bar_width, draw_info.height))         

# creating starting list function for our program 

def generate_start_list(n, min_val, max_val): 
    lst = [] 
    # do this n number of times 
    for _ in range(n): 
        val = random.randint(min_val, max_val)
        lst.append(val) 

    # the new list is now generated 
    return lst  


# this is our main function to show what we have currently 
def main(): 

    run = True 
    clock = pygame.time.Clock()
     
    # values can be assigned easily 
    n = 50 
    min_val = 0
    max_val = 100 

    lst = generate_start_list(n, min_val, max_val) 

    # in pygame, must have a constant loop running 
    # for example, if you draw something on screen, program will draw and then immediately end
    # we do not want this, we want it to continously run UNTIL we end it manually  
     
    draw_info = globalValues(1000, 800, lst)
    while run:  
        #number of frames
        clock.tick(60) 
        draw(draw_info)
        pygame.display.update() 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type != pygame.KEYDOWN:
                continue 
            
            if event.key == pygame.K_r:
                lst = generate_start_list(n, min_val, max_val)
                draw_info.set_list(lst) 

    # as soon run is False, the program will be stopped 
    pygame.quit()  

if __name__ == "__main__":
    main()

