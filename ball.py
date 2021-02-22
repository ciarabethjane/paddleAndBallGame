import pygame
pygame.init()

class Ball:

    def __init__(self, x, y, color, radius, speed_x, speed_y):
        self.__x = x
        self.__y = y
        self.__coordinates = [x, y]
        self.__color = color
        self.__radius = radius
        self.__speed_x = speed_x 
        self.__speed_y = speed_y # controlling the "speed" of the ball
    
    #This method draws the circle on screen
    def draw(self, display):
        pygame.draw.circle(display, self.__color, self.__coordinates, self.__radius)

    def move(self, displayWidth, displayHeight):
        #Indicator that the ball has reached the bottom of the screen (which is protected by the paddle) and to reset to the middle of the screen
        #Because circles are drawn from the centre, to stop the circle from partially disappearing off-screen, if self.__x is equal to the display height minus the radius of the circle, it should be treated as if it has hit the bottom of the screen
        if self.__y == (displayHeight - self.__radius):
            self.__x = 250
            self.__y = 250
        #indicator that the ball has hit the top of the screen and to change speed in order to change direction
        if self.__y == (0 + self.__radius):
            self.__speed_y =  - self.__speed_y
            self.__speed_x = - self.__speed_x
        #indicator that the ball has hit the left side of the screen and to change speed in order to change direction
        if self.__x == (0 + self.__radius):
            self.__speed_y =  - self.__speed_y
            self.__speed_x =  - self.__speed_x
        #indicator that the ball has hit the right side of the screen and to change speed in order to change direction
        if self.__x == (500 - self.__radius):
            self.__speed_x =  - self.__speed_x
            self.__speed_y = - self.__speed_y
        #indicator that the ball has hit the top right corner and to change speed to change direction
        if self.__x == (500 - self.__radius) and self.__y == (0 + self.__radius):
            self.__speed_x =  - self.__speed_x
            self.__speed_y = - self.__speed_y
        #indicator that the ball has hit the top left corner and to change speed to change direction
        if self.__x == (0 + self.__radius) and self.__y == (500 - self.__radius):
            self.__speed_x =  - self.__speed_x
            self.__speed_y = - self.__speed_y
        #If none of the above conditions are true, the ball has not hit any of the sides of the screen, and the ball should maintain the same speed
        else:
            self.__speed_y = self.__speed_y
            self.__speed_x = self.__speed_x
        #Executing the actual movement
        self.__y = self.__y - self.__speed_y
        self.__x = self.__x + self.__speed_x
        self.__coordinates = [self.__x,self.__y]

    def set_direction_up(self):
        #Because I'm only controlling an Upward movement in this method, I only need to manipulate the Y value
        #I will use the getter methods from the paddle class in main.py to determine if the ball and paddle have collided
        #If they have collided, this method will be called
        self.__speed_y = - self.__speed_y
    
    #Getter method for the ball's x coordinate
    def get_ball_x(self):
        return self.__x

    #Getter method for the ball's y coordinate
    def get_ball_y(self):
        return self.__y

    #Getter method for the ball's radius
    def get_ball_radius(self):
        return self.__radius     

   