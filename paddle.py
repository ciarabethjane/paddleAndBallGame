import pygame
pygame.init()

class Paddle():
    #Creating the  width and height of the paddle as private class variables, because I want the paddle to remain the same size in every instance of the class
    __paddleWidth = 300
    __paddleHeight = 20

    def __init__(self, x, y, color, speed_x):
        #Creating the coordinates of the paddle as instance variables, because the coordinates of the paddle need to be able to change with each instance of the class
        #All instance variables are being created as private variables so that they cannot be accessed outside of the paddle class, to avoid confusion with similarly named variables in the Ball class
        self.__x = x 
        self.__y = y 
        self.__coordinates = [self.__x, self.__y, self.__paddleWidth, self.__paddleHeight]
        #Creating the speed and colour of the paddle as an instance variable so that the speed can be changed if desired without having to access the class code outside of main.py
        self.__color = color 
        #Creating an original speed variable. This will be used to revert the paddle's speed back to it's original speed after it has been stopped and the user has changed it's direction because it was trying to move off screen.
        self.__original_speed = speed_x
        self.__speed = speed_x
        

    #Draw the paddle on screen
    def draw(self, display):
        pygame.draw.rect(display, self.__color, self.__coordinates, 0)

    #Method that controls the left-ward movement of the paddle
    def move_left(self, moveleft_trigger):
        #Indicator that the paddle has reached the left side of the screen and to change speed in order to change direction so it won't exit the screen
        #Because rectangles are drawn from the top left corner, if self.__x == 0, that means the edge of the paddle is at the left edge of the screen and needs to stop
        if self.__x == 0:
            self.__speed = 0
        else:
            #Using the original_speed variable here ensures that if the user had used the move_right method previously and the speed was changed to 0 to stop
            #the paddle from going off screen, the speed reverts to the speed it should be moving at when it's not stopped at the edge of the screen
             self.__speed = self.__original_speed
        #Executing the actual movement
        self.__x = self.__x - self.__speed
        self.__coordinates = [self.__x,self.__y, self.__paddleWidth, self.__paddleHeight]
    
    #Method that controls the right-ward movement of the paddle
    def move_right(self, display_width, moveright_trigger):
        #Indicator that the paddle has reached the right side of the screen and to change speed in order to change direction so it won't exit the screen
        #Because rectangles are drawn from the top left corner, when self.__x is the full length of the paddle away from the edge of the screen, the paddle
        #needs to stop moving or it will partially disappear off-screen. Changing the speed to 0 stops the paddle from moving.
        if self.__x >= (display_width - self.__paddleWidth):
            self.__speed = 0
            self.__display_width = display_width
        else:
            #Using the original_speed variable here ensures that if the user had used the move_right method previously and the speed was changed to 0 to stop
            #the paddle from going off screen, the speed reverts to the speed it should be moving at when it's not stopped at the edge of the screen
            self.__speed = self.__original_speed
        #Executing the actual movement
        self.__x = self.__x + self.__speed
        self.__coordinates = [self.__x,self.__y, self.__paddleWidth, self.__paddleHeight]

    #Getter method for the x position of the paddle on the screen
    def get_screen_x(self):
        return self.__x

    #Getter method for the y position of the paddle on the screen
    def get_screen_y(self):
        return self.__y

    #The getter methods for both the screen width and height is based on code that I found here: https://stackoverflow.com/questions/36653519/how-do-i-get-the-size-width-x-height-of-my-pygame-window
    #After I saw the piece of code from the above link, I thought it would be more effective to just get the width in the getter method for the width of the screen, and just getting the height in the getter 
    # method for the height method of the screen, so I searched for built-in methods relating to surface size in the pygame documentation and learned about the get_width() and get_height() methods. I combined 
    # the information from the documentation and used it to adapt the code I found on the Stack Overflow to make it more specific to the task I wanted to achieve using the getter methods. The pygame documentation 
    #I used can be found here: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_size

    #Getter method for the width of the screen
    def get_screen_width(self):
        width_of_screen = pygame.display.get_surface().get_width()
        return width_of_screen

    #Getter method for the height of the screen
    def get_screen_height(self):
        height_of_screen = pygame.display.get_surface().get_height()
        return height_of_screen