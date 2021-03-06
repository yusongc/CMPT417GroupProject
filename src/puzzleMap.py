import pygame, sys, random
import puzzle, search
from pygame.locals import *

# some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (150, 75, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# screen basic parameters
width = 500
height = 500
block_size = 100

pygame.init()
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('3x3 Sliding Puzzle')
button_Astar = pygame.Rect(60, 350, 60, 30)
button_BFS = pygame.Rect(150, 350, 60, 30)
button_DFS = pygame.Rect(240, 350, 60, 30)
button_IDAstar = pygame.Rect(330, 350, 60, 30)
button_IDDFS = pygame.Rect(60, 400, 60, 30)
big_font = pygame.font.Font('freesansbold.ttf', 32)
small_font = pygame.font.Font(None, 25)

# Just for test, need import more cases
# TODO: how to combine our code? also need to uniform the format
puzzle = [2, 5, 4, 7, ' ', 3, 8, 1, 6]

# Create a timer
clock = pygame.time.Clock()
frame_rate = 60
time_count = 0

click = False

while True:
    # Handle the exit case
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button_Astar.collidepoint(mouse_pos):
                #search.a_star_search(puzzle)
                click = True
            elif button_BFS.collidepoint(mouse_pos):
                #search.breadth_first_search(puzzle)
                click = True
            elif button_DFS.collidepoint(mouse_pos):
                #search.breadth_first_search(puzzle)
                click = True
    
    window.fill(WHITE)

    i = 0
    margin_y = 1
    for y in range(3):
        margin_x = 1
        for x in range(3):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(window, BLACK, rect, 1)
            text = big_font.render(str(puzzle[i]), True, BLACK)
            coordinate = (block_size*margin_x // 2, block_size*margin_y // 2)
            window.blit(text, coordinate)
            i += 1
            margin_x += 2
        margin_y += 2
    
    # Doing the time count
    if click == True:
        total_seconds = time_count // frame_rate
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_time = "{0:02}:{1:02}".format(minutes, seconds)
        time_text = small_font.render(output_time, True, BLACK)
        pygame.draw.ellipse(window, RED, [330, 85, 80, 50], 5)
        window.blit(time_text, [350, 100])
        
        time_count += 1
        clock.tick(frame_rate)

    # Draw different algo rects
    pygame.draw.rect(window, BROWN, button_Astar)
    pygame.draw.rect(window, BROWN, button_BFS)
    pygame.draw.rect(window, BROWN, button_DFS)
    pygame.draw.rect(window, BROWN, button_IDAstar)
    pygame.draw.rect(window, BROWN, button_IDDFS)
    astar = small_font.render("A*", True, WHITE)
    bfs = small_font.render("BFS", True, WHITE)
    dfs = small_font.render("DFS", True, WHITE)
    ida_star = small_font.render("IDA*", True, WHITE)
    iddfs = small_font.render("IDDFS", True, WHITE)
    window.blit(astar, [80, 360])
    window.blit(bfs, [160, 360])
    window.blit(dfs, [250, 360])
    window.blit(ida_star, [340, 360])
    window.blit(iddfs, [65, 410])

    pygame.display.flip()