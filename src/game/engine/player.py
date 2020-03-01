import pygame  # type: ignore
import os
import pathlib

PATH_TO_DIR = pathlib.Path(__file__).parent.parent.parent.absolute()


class Player:
    """
    Player class allows for movement of player character and rendering

    Parameters
    ----------

    position: pygame.Rect
         Pygame representation of a Rectangle

    image_path: str
         path to image to use as player image
    """

    position: pygame.Rect

    image: pygame.image

    def __init__(self, position, image_path: str):

        self.position = position
        self.image = pygame.transform.scale(
            pygame.image.load(
                f"{PATH_TO_DIR}{os.sep}assets{os.sep}game{os.sep}whiteSquare.png"
            ),
            (position.width, position.height),
        )
        self.controls = {pygame.K_RIGHT: self.right, pygame.K_SPACE: self.jump}

    def is_collided_with(self, sprite):
        return self.position.colliderect(sprite.position)

    def jump(self):
        """
        Makes the player jump into the air

        TODO: gravity and physics
        """
        self.position = self.position.move(0, -10)

    def right(self):
        """
        Moves the Player to the Right by a constant factor
        """
        self.position = self.position.move(10, 0)

    def draw(self, screen):
        """
        Renders the Player as a Rectangle

        Parameters
        ----------

        screen: Any
             The screen to draw the player onto
        """
        screen.blit(self.image, self.position)