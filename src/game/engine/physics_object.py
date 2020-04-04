from .game_object import GameObject
import pygame


class PhysicsObject(GameObject):

    """
    PhysicsObject

    Parameters
    ----------

    x_vel: float
    initial x velocity

    y_vel: float
        initial y velocity
    """

    def __init__(
        self, position: pygame.Rect, image_path: str, x_vel: float, y_vel: float
    ):
        super().__init__(position, image_path)
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.gravity = 1.0

    def update(self) -> None:
        """
        Update the position of this object based on its velocity values.
        """
        self.position.x += self.x_vel
        self.position.y += self.y_vel + self.gravity

    def handle_collision(self, otherPhysicsObject):
        """
        Stub to be implemented in child classes
        """
        pass
