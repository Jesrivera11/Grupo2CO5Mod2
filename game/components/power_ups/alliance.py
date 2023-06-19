from game.components.power_ups.power_up import PowerUp
from game.utils.constants import ALLIANCE_TYPE, ALLIANCE

class Alliance(PowerUp):
    def __init__(self):
        super().__init__(ALLIANCE, ALLIANCE_TYPE)