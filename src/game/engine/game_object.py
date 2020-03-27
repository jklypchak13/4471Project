"""
Base Game Object

Goals
-----

Detecting Collision

Rendering

Non-Goals
---------

Handle movement
      GameObjects immediate subclasses are static objects, reference PhyiscsObject
      for moving objects
"""
from typing import Tuple

import pygame  # type: ignore


class GameObject:
    """
    GameObject

    Parameters
    ----------

    position: pygame.Rect
          Pygame representation of (x, y, width, height)

    image_path: str
          Path to image
    """

    position: pygame.Rect
    image: pygame.Image

    def __init__(self, position: pygame.Rect, image_path: str):
        self.position = position
        self.image = pygame.transform.scale(
            pygame.image.load(image_path), (self.position.width, self.position.height)
        )

    def draw(self, screen: pygame.Surface, screen_offset: Tuple[int, int]) -> None:
        """
        Renders the GameObject to the screen

        Parameters
        ----------

        screen: pygame.Surface
              Screen to draw to

        screen_offset
              Offset of the screen
        """
        screen.blit(self.image, self.position)

    def __contains__(self, game_object: GameObject) -> bool:
        """
        Detects a collision between self and another GameObject

        Parameters
        ----------

        game_object: GameObject
              Detects if they've collided

        Returns
        -------

        bool
              True if they have, false otherwise
        """
        return self.position.collderect(game_object.position)
