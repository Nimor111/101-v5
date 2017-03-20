import unittest
from panda_social_network import PandaSocialNetwork, Panda


class PandaSocialNetworkTests(unittest.TestCase):

    def setUp(self):
        self.panda_social_network = PandaSocialNetwork()

    def test_panda_name_method_avoids_collision(self):
        panda = Panda('name', '1@hb.com', 'male')
        self.assertEqual(panda.name(), 'name')

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

        level = self.panda_social_network. \
            connection_level(panda1, panda4)
        self.assertEqual(3, level)
        # self.assertEqual([panda1, panda2, panda3, panda4], list(path))

    def test_connection_level_for_two_pandas_who_are_not_connected(self):
        panda1 = Panda('name', '1@hb.com', 'male')
        panda2 = Panda('name', '2@hb.com', 'male')

        self.panda_social_network.add_panda(panda1)
        self.panda_social_network.add_panda(panda2)

        self.assertEqual(self.panda_social_network.
                         connection_level(panda1, panda2), -1)

    def test_friends_of_panda_with_two_friends(self):
        panda1 = Panda('name', '1@hb.com', 'male')
        panda2 = Panda('name', '2@hb.com', 'male')
        panda3 = Panda('name', '3@hb.com', 'male')

        self.panda_social_network.make_friends(panda1, panda2)
        self.panda_social_network.make_friends(panda1, panda3)

        self.assertEqual(self.panda_social_network.friends_of(panda1),
                         set([panda2, panda3]))

    def test_are_connected_two_pandas_that_are(self):
        panda1 = Panda('name', '1@hb.com', 'male')
        panda2 = Panda('name', '2@hb.com', 'male')

        self.panda_social_network.make_friends(panda1, panda2)
        self.assertTrue(self.panda_social_network.
                        are_connected(panda1, panda2))

    def test_gender_when_level_is_0(self):
        panda1 = Panda('name', '1@hb.com', 'male')
        panda2 = Panda('name', '2@hb.com', 'male')
        panda3 = Panda('name', '3@hb.com', 'male')

        self.panda_social_network.make_friends(panda1, panda2)
        self.panda_social_network.make_friends(panda1, panda3)
        self.assertEqual(self.panda_social_network.how_many_gender_in_network
                         (1, panda1, 'male'), 2)

    def test_friends_of_panda_with_0_friends(self):
        panda1 = Panda('name', '1@hb.com', 'male')
        self.panda_social_network.add_panda(panda1)
        self.assertEqual(self.panda_social_network.friends_of(panda1),
                         set())


if __name__ == '__main__':
    unittest.main()
