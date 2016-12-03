import unittest
from panda_social_network import PandaSocialNetwork, Panda


class PandaSocialNetworkTests(unittest.TestCase):

    def setUp(self):
        self.panda_social_network = PandaSocialNetwork()

    def test_get_pandas_return_1_panda_if_1_panda_is_added(self):
        panda = Panda('Pesho', 'pesho@hackbulgaria.com', 'male')
        self.panda_social_network.add_panda(panda)
        self.assertEqual(self.panda_social_network.get_pandas(), [panda])

    def test_make_friends_work_properly(self):
        panda1 = Panda('Pesho', 'pesho@hackbulgaria.com', 'male')
        panda2 = Panda('Peshoze', 'peshov@hackbulgaria.com', 'male')
        self.assertEqual(0, len(self.panda_social_network.get_pandas()))
        self.panda_social_network.make_friends(panda1, panda2)
        self.assertEqual(2, len(self.panda_social_network.get_pandas()))
        self.assertTrue(self.panda_social_network.are_friends(panda1, panda2))
        self.assertTrue(self.panda_social_network.are_friends(panda2, panda1))

    def test_connection_level_for_graph_with_4_pandas(self):
        panda1 = Panda('name', '1@hb.com', 'male')
        panda2 = Panda('name', '2@hb.com', 'male')
        panda3 = Panda('name', '3@hb.com', 'male')
        panda4 = Panda('name', '4@hb.com', 'male')
        self.panda_social_network.make_friends(panda1, panda2)
        self.panda_social_network.make_friends(panda2, panda3)
        self.panda_social_network.make_friends(panda3, panda4)

        self.assertEqual(self.panda_social_network.
                         connection_level(panda1, panda3), (2, [panda1, panda2, panda3]))
        self.assertEqual(self.panda_social_network.
                         connection_level(panda1, panda4), 3, [panda1, panda2, panda3])
        self.assertEqual(self.panda_social_network.
                         connection_level(panda1, panda1), 0, [])
        self.assertEqual(self.panda_social_network.
                         connection_level(panda1, panda2), 1, [panda1, panda2])

    def test_connection_level_for_two_pandas_who_are_not_connected(self):
        panda1 = Panda('name', '1@hb.com', 'male')
        panda2 = Panda('name', '2@hb.com', 'male')

        self.panda_social_network.add_panda(panda1)
        self.panda_social_network.add_panda(panda2)

        self.assertIsNone(self.panda_social_network.
                          connection_level(panda1, panda2))


if __name__ == '__main__':
    unittest.main()
