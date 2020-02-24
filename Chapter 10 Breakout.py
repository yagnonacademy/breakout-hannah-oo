#-----------------------------------------------------------------------------------------
#                                   Breakout
#
#       Created by: Hannah
#       Created on: 23 January 2020
#
#       This program will be execute the breakout game file. (a ball hitting blocks
#       on the ceiling and getting points for it)
#
#-----------------------------------------------------------------------------------------
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

def moving_rect(screen, x, y):
    pygame.draw.rect(screen,WHITE,[x, y,90,20],0)

def bricks(screen, x, y):
    pygame.draw.rect(screen, WHITE, [x, y, 90, 30], 0)

def ball(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y, 20, 20],0)

def gameover_sentence(screen, x, y):
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, [x, y])
    
def main():
    
    pygame.init()
     
    # Set the width and height of the screen [width, height]
    size = (575, 600)
    screen = pygame.display.set_mode(size)
     
    pygame.display.set_caption("Breakout")

    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Speed of pallet/moving rect in pixels per frame
    x_speed = 0
    y_speed = 0
     
    # Current position of pallet/moving rect
    x_coord = 240
    y_coord = 510

    # Speed of the ball
    ball_change_x = 0
    ball_change_y = 0

    # Ball position at the start
    ball_x = 275
    ball_y = 490

    # Score board
    score = 0

    x_position_brick = [5, 100, 195, 290, 385, 480]
    notStarted = True

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
        # User pressed down on a key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5        
                elif event.key == pygame.K_SPACE and notStarted:
                    ball_change_x = 3
                    ball_change_y = -3
                    notStarted = False
         
            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                    
        ## Game Logic ##
                    
        # Move the paddle according to the speed vector.
        x_coord += x_speed
        y_coord += y_speed
        if x_coord >= 485 or x_coord <= 0:
            x_speed = 0

        # Position of the ball while moving
        ball_x += ball_change_x
        ball_y += ball_change_y

        # Bouncing the ball off the wall
        if ball_x >= 555 or ball_x <= 0:
            ball_change_x = -ball_change_x
        if ball_y <= 0:
            ball_change_y = -ball_change_y

        # Bouncing the ball off the paddle
        if ball_y <= 510 and ball_y +20 >= 511:
            if x_coord <= ball_x <= x_coord+ 90:
                ball_change_y = -ball_change_y

        # Bouncing the ball off the bricks
        for i in x_position_brick:
            if i <= ball_x <= i+ 90 and ball_y <= 35:
                ball_change_y = -ball_change_y
                x_position_brick.remove(i)
                score += 10
                
        # Black background 
        screen.fill(BLACK)
     
        # Drawing codes
        moving_rect(screen, x_coord, y_coord)
        ball(screen, ball_x, ball_y)
        # Drawing bricks
        for i in x_position_brick:
            pygame.draw.rect(screen, WHITE, [i, 5, 90, 30], 0)

        # Losing life and game over sentence
        if ball_y >= 600:
            gameover_sentence(screen, 235, 250)
            
        # You win sentence
        if x_position_brick == []:
            ball_change_y = 0
            ball_change_x = 0
            font = pygame.font.SysFont('Calibri', 25, True, False)
            text = font.render("Congratulation!", True, WHITE)
            screen.blit(text, [210, 250])        

        # Score
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Score: " + str(score),  True, WHITE)
        screen.blit(text, [30, 570])
        
        # fliping the screen
        pygame.display.flip()

        clock.tick(60)
     
    pygame.quit()

main()
