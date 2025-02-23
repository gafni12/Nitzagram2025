import pygame

from constants import *
from helpers import *
from .Post import Post

class TextPost(Post):
    def __init__(self,username, location, description, text, text_color, background_color):
        super().__init__(username, location, description)
        self.background_color = background_color
        self.text_color = text_color
        self.text_array = from_text_to_array(text)
    def display_content(self):
        square = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, square)

        for i in range(0, len(self.text_array)):
            font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
            text = font.render(self.text_array[i], True, self.text_color)
            text_pos = center_text(len(self.text_array),text, i)
            screen.blit(text, text_pos)

