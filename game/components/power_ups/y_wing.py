from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SPACESHIP, YWING_TYPE

class Ywing(PowerUp):
    def __init__(self):
        super().__init__(SPACESHIP, YWING_TYPE)