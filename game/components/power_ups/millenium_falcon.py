from game.components.power_ups.power_up import PowerUp
from game.utils.constants import MILLENIUM, MILLENIUM_TYPE


class MilleniumFalcon(PowerUp):
    def __init__(self):
        super().__init__(MILLENIUM, MILLENIUM_TYPE)