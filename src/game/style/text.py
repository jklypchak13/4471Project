import pygame


# initialize fonts
pygame.font.init()

# =============================================================================
# Font Styles
# =============================================================================
default_font = pygame.font.SysFont(pygame.font.get_fonts()[0], 20)
menu_title = pygame.font.SysFont(pygame.font.get_fonts()[0], 100)
menu_button = pygame.font.SysFont(pygame.font.get_fonts()[0], 30)
hacked_title = pygame.font.SysFont("centuryschoolbook", 50)
fancy_title = pygame.font.SysFont("centuryschoolbook", 50)
fancy_sub_title = pygame.font.SysFont("centuryschoolbook", 24)
