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

    walk_speed:float = 1.0

    def update(self):
        """
        Set this enemy's horizontal velocity based on their walking speed.
        Call PhysicsObject update method.
        """
        x_vel = walk_speed
        super().update()

    def handle_player_collision(self, player: Player) -> None:
        """
        Handle collision logic with Player. Kill the player.

        Parameters
        ----------

        player: Player
             Reference to the player that has been collided with.
        """
        player.kill()

    def flip_direction(self) -> None:
        """
        Change the enemy's walking direction from right to left or vice versa.
        """
        self.walk_speed *= -1

    def kill(self) -> None:
        """
        Kill this enemy
        """
        #todo remove self from all game_objects lists
        #TODOLATER death animation?
        pass