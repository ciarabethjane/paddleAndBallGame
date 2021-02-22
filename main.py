import pygame
#Import the Ball class from ball.py
from ball import Ball 
#Import the Paddle class from paddle.py
from paddle import Paddle

pygame.init()

#Set up pygame display
displayWidth = 500
displayHeight = 500
displaySize = [displayWidth, displayHeight]
display = pygame.display.set_mode(displaySize)

#setup for colours
black = [0,0,0]
blue = [27,130,209]
yellow = [255,255,0]


#Initialise time for game framerate
clock = pygame.time.Clock()

#create an instance of the paddle class
gamePaddle = Paddle(200, 480, blue, 20)

#create and instance of the ball class
gameBall = Ball(250, 250, yellow, 40, 5, 5)

run_game = True
#Create game loop
while run_game:
    display.fill(black)
    #draw the gamePaddle on the display
    gamePaddle.draw(display)
    #draw the ball on the display
    gameBall.draw(display)
    #move the gameBall
    gameBall.move(500, 500)

    #I learned about the key.set_repeat() in the pygame documentation, and then used information on this page https://stackoverflow.com/questions/18995652/pygame-key-set-repeat-not-working to troubleshoot getting it to work
    #The  initial mistake I made was placing it inside each if statement that related to the key presses
    #This line of code will generate multiple pygame.KEYDOWN events when the user continues to hold down a key 
    #This is how the paddle will continue to move when the user has the appropriate key pressed and stop moving when released
    pygame.key.set_repeat(1,10)

    #The pygame event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        #if a key on the keyboard is pressed down check if it's the left or right arrow key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #if it's the left arrow key, implement the move_left() method to move the gamePaddle to the left
                gamePaddle.move_left(pygame.K_LEFT)
            if event.key == pygame.K_RIGHT:
                #if it's the right arrow key, implement the move_right() method to move the gamePaddle to the right
                gamePaddle.move_right(500, pygame.K_RIGHT)
    
    #This if statement calculates if the ball has hit the paddle. 
    # If it has, it calls the set_direction_up() method from the Ball class to get the gameBall to move upward
    if gamePaddle.get_screen_x() + gameBall.get_ball_radius() == gameBall.get_ball_x() or gamePaddle.get_screen_y() - gameBall.get_ball_radius() == gameBall.get_ball_y():
        gameBall.set_direction_up()
    #testing the getter methods in the paddle class
    print("paddle x position = ", gamePaddle.get_screen_x())
    print("paddle y position = ", gamePaddle.get_screen_y())
    print("screen width = ", gamePaddle.get_screen_width())
    print("screen height = ", gamePaddle.get_screen_height())
        
    #Update the pygame display window
    pygame.display.update()
    clock.tick(45)

#quit pygame
pygame.quit()
quit()