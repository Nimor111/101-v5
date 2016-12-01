from panda import Panda
from panda_already_there import PandaAlreadyThereError


class PandaSocialNetwork:

    def __init__(self):
        self.social_network = {}

    def add_panda(self, panda):
        if panda in self.social_network:
            raise PandaAlreadyThereError('Panda is already in the network!')
        self.social_network[panda] = []
        return self.social_network

    def has_panda(self, panda):
        return bool(panda in self.social_network)

    def make_friends(self, panda1, panda2):
        pass


panda = Panda('Ivo', 'georgi.bojinov@hotmail.com', 'male')
panda2 = Panda('Iva', 'georgina.bozhinov@hotmail.com', 'female')

psn = PandaSocialNetwork()
psn.add_panda(panda)
psn.add_panda(panda)
