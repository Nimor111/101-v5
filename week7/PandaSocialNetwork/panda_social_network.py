import json
from panda import Panda
from panda_already_there import PandaAlreadyThereError
from collections import deque


class PandaSocialNetwork:

    def __init__(self):
        self.social_network = {}

    def get_pandas(self):
        return list(self.social_network.keys())

    def add_panda(self, panda):
        if self.has_panda(panda):
            return
        self.social_network[panda] = set()
        return self.social_network

    def has_panda(self, panda):
        return panda in self.social_network

    def make_friends(self, panda1, panda2):
        self.add_panda(panda1)
        self.add_panda(panda2)

        self.social_network[panda1].add(panda2)
        self.social_network[panda2].add(panda1)
        return self.social_network

    def are_friends(self, panda1, panda2):
        check1 = panda1 in self.social_network[panda2]
        check2 = panda2 in self.social_network[panda1]

        if check1 and not check2 or check2 and not check1:
            raise AssertionError('Something\'s wrong with the graph')

        return check1 and check2

    def friends_of(self, panda):
        if panda not in self.social_network:
            return False
        return self.social_network[panda]

    def connection_level(self, start, target):  # bfs
        q = deque()
        visited = set()
        paths = {start: None}

        q.append((0, start))
        visited.add(start)

        while q:
            level, current = q.popleft()

            if current == target:
                path = []

                while target is not None:
                    path.append(target)
                    target = paths[target]

                return (level, list(reversed(path)))
                # path = {str(key): str(value) for key, value in path.items()}
                # print(json.dumps(path, indent=4))

            for neigh in self.social_network[current]:
                if neigh not in visited:
                    q.append((level + 1, neigh))
                    visited.add(neigh)
                    paths[neigh] = current

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) is not None

    def bfs(self, panda, t_level):
        queue = deque()
        visited = set()

        queue.append((0, panda))
        visited.add(panda)

        while queue:
            level, current = queue.popleft()

            if level == t_level:
                print("Found it")
                nodes = [current]

                for elem in queue:
                    nodes.append(elem[1])

                return nodes

            for neigh in self.social_network[current]:
                if neigh not in visited:
                    queue.append((level + 1, neigh))
                    visited.add(neigh)

    def how_many_gender_in_network(self, level, panda, gender):
        return sum([1 for child in self.bfs(panda, level) if child.gender ==
                    gender])


panda = Panda('name', '1@hb.com', 'male')
panda2 = Panda('name', '2@hb.com', 'male')
panda3 = Panda('name', '3@hb.com', 'male')
sn = PandaSocialNetwork()
sn.make_friends(panda, panda2)
sn.make_friends(panda, panda3)
print(sn.bfs(panda, 1))
