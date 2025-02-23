import pygame

from constants import *
from helpers import screen

class Comment:
    def __init__(self, text):
        self.text = text

    def display(self, comment_number):

        font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        text = font.render(self.text, True, BLACK)
        screen.blit(text, [FIRST_COMMENT_X_POS, (FIRST_COMMENT_Y_POS + (COMMENT_LINE_HEIGHT * comment_number))])




