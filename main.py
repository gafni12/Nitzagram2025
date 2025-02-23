import pygame
from helpers import *
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from buttons import *
from classes.ImagePost import ImagePost
from classes.TextPost import TextPost

def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    posts = [
        ImagePost("Noa Kirel", "Dubai", "I love Dubai!", "Images/noa_kirel.jpg"),
        ImagePost("Ronaldo", "Portugal", "Messi is better!!", "Images/ronaldo.jpg"),
        TextPost("Gafni_Carmi", "California", "Help", "Where am i sleeping today", BLACK, (255, 255, 255),)
    ]

    display_index = 0

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_in_button(click_post_button, mouse_pos):
                    if display_index >= len(posts) - 1:
                        display_index = 0
                    else:
                        display_index += 1
                if mouse_in_button(like_button, mouse_pos):
                    posts[display_index].add_like()
                if mouse_in_button(comment_button, mouse_pos):
                    posts[display_index].add_comment(read_comment_from_user())
                if mouse_in_button(view_more_comments_button, mouse_pos):
                    posts[display_index].view_more_comments()


        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        posts[display_index].display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)



    pygame.quit()
    quit()


main()
