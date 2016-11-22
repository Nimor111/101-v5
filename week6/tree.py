from queue import Queue


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
        if Tree.find_child(self.root, x):
            return True
        return False
    """
        Returns True or False if Node with value x is present in the tree
    """
    def get_height_node(self, node):
        if node == self.root.value:
            return 0
        if node.is_leaf() is False:
            return 1
        for child in node.children:
            return 1 + self.get_height_node(child)

    def BFS(self):  # implements BFS with queue yay
        counter = 0
        splicer = '|'
        queue = Queue()
        list_of_children = []
        temp_list = []
        if self.root:
            queue.enqueue(self.root)
            list_of_children.append([self.root.value])
        else:
            raise "Empty tree!"
        queue.enqueue(splicer)
        while not queue.empty():
            value = queue.dequeue()
            if value == splicer:
                if temp_list != []:
                    list_of_children.append(temp_list)
                temp_list = []
                counter += 1
                if queue.empty():
                    return (counter - 1, list_of_children)
                else:
                    queue.enqueue(splicer)
            else:
                for child in value.children:
                    queue.enqueue(child)
                    temp_list.append(child.value)

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
        Returns the number of node sin the tree
        In our example -> tree.count_nodes() = 4
    """

    def tree_levels(self):
        return self.BFS()[1]
    """
        Returns a list of lists with the nodes foe each level1
        tree.tree_levels = [[5], [4, 3], [2]]
    """


tree = Tree(5)
tree.add_child(5, 4)
tree.add_child(4, 3)
tree.add_child(5, 6)
tree.add_child(4, 2)
print(tree.find(4))
print(tree.nodes)
print(tree.height())
print(tree.tree_levels())
# print(tree.get_height_node(Tree.find_child(tree.root, 3)))
