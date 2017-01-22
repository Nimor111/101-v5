from models.world_object import WorldObject


class Food(WorldObject):

    def __init__(self, name="Banana", energy=4):
        self.energy = energy
        self.name = name
