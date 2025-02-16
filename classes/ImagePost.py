import pygame

from constants import *
from helpers import screen
from Post import Post
class ImagePost(Post):

    def __int__(self, username, location, description, image_src):
        super().__init__(username, location, description)
        img = pygame.image.load(image_src)
        img = pygame.transform.scale(img, (POST_WIDTH, POST_HEIGHT))
        self.image = img

    def display_content(self):
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))