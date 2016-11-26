from queue import Queue
from stack import Stack


class TreeNode:

    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def is_leaf(self):
        return len(self.children) == 0


class Tree:

    def __init__(self, root=None):
        self.root = TreeNode(root)
        self.nodes = 1
    """
    When we are creating a new tree, we must always have a root element.
    For example:
    tree = Tree(root=5)
    """

    def add_child(self, parent, child):
        parent_node = self.find_child(self.root, parent)
        if parent_node:
            parent_node.add_child(TreeNode(child))
            self.nodes += 1
            return True
        return False
    """
    When we are adding new element to our tree, we must specify the parent:
    tree = Tree(root=5)
    tree.add(parent=5, child=4)
    tree.add(parent=5, child=3)
    tree.add(parent=4, child=2)

    This will make the following tree:

        5
       / \
      4   3
     /
    2
    """
    @staticmethod
    def find_child(node, x):
        if x == node.value:
            return node
        if node.is_leaf():
            return False
        for child in node.children:
            c = Tree.find_child(child, x)
            if c:
                return c
        return False

    def find(self, x):
        return bool(Tree.find_child(self.root, x))
    """
        Returns True or False if Node with value x is present in the tree
    """

    def BFS(self):  # implements BFS with queue yay
        splicer = '|'
        queue = Queue()
        level_count = 0
        levels = {level_count: [self.root.value]}
        if self.root:
            queue.enqueue(self.root)
        else:
            raise "Empty tree!"
        queue.enqueue(splicer)
        level_count += 1
        levels[level_count] = []
        while not queue.empty():
            value = queue.dequeue()
            if value == splicer:
                if queue.empty():
                    levels.pop(len(levels.keys()) - 1)
                    return (len(levels.keys()) - 1, levels)
                else:
                    level_count += 1
                    levels[level_count] = []
                    queue.enqueue(splicer)
            else:
                for child in value.children:
                    queue.enqueue(child)
                    levels[level_count].append(child.value)

    def DFS(self, node):
        stack = Stack()
        stack.push(node)
        res = []
        while stack.empty() is False:
            curr = stack.pop()
            res.append(curr.value)

            for child in curr.children:
                stack.push(child)
        return res

    def height(self):
        return self.BFS()[0]
    """
        Returns an integer number of the max height of the tree
          5
         / \
        4   3
       /
      2

      tree.height() = 2
    """

    def count_nodes(self):
        return self.nodes
    """
        Returns the number of nodes in the tree
        In our example -> tree.count_nodes() = 4
    """

    def tree_levels(self):
        return list(self.BFS()[1].values())
    """
        Returns a list of lists with the nodes foe each level1
        tree.tree_levels = [[5], [4, 3], [2]]
    """


def main():
    pass


if __name__ == '__main__':
    main()
