import pygame

from constants import *
from helpers import screen
from Post import Post

class Comment:
    def __int__(self, text):
        self.text = text

    def display_comment(self, comment_number):

        font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        text = font.render(self.text, True, BLACK)
        screen.blit(text, [FIRST_COMMENT_X_POS, (FIRST_COMMENT_Y_POS + (COMMENT_LINE_HEIGHT * comment_number))])




