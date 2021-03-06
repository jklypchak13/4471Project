import pygame

from .physics_object import PhysicsObject
from .player import Player


class Enemy(PhysicsObject):

    """
    Enemy

    Parameters
    ----------

    walk_speed: float
        enemy walking speed
    """

    def __init__(
        self, position: pygame.Rect, image_path: str, x_vel: float, y_vel: float
    ):
        super().__init__(position, image_path, x_vel, y_vel)

    def handle_player_collision(self, player: Player) -> None:
        """
        Handle collision logic with Player. Kill the player.

        Parameters
        ----------

        player: Player
             Reference to the player that has been collided with.
        """
        player.hit()

    def flip_direction(self) -> None:
        """
        Change the enemy's walking direction from right to left or vice versa.
        """

        if self.frames is not None:
            flipped_frames = []
            for frame in self.frames:
                flipped_frames.append(
                    pygame.transform.flip(frame, True, False))
            self.frames = flipped_frames

        self.x_vel *= -1

    def kill(self) -> None:
        """
        Kill this enemy
        """
        # todo remove self from all game_objects lists
        # TODOLATER death animation?
        pass
