# leap frogs game in Python

from collections import deque


class Tree:
    class TreeNode:
        def __init__(self, value, children=None):
            if children is None:
                children = []

            self.value = value
            self.children = children
            self.level = 0

    def __init__(self, root):
        self.__root = self.TreeNode(root)
        self.__size = 1

    def root(self):
        return self.__root

    def __find(self, value):
        stack = deque()
        stack.append(self.__root)

        while len(stack) != 0:
            current_node = stack.pop()

            if current_node.value == value:
                return current_node

            for child in current_node.children:
                stack.append(child)

    def DFS(self, node):
        stack = deque()
        stack.append(node)
        res = []
        while len(stack) != 0:
            curr = stack.pop()
            res.append(curr.value)

            for child in curr.children:
                stack.append(child)
        return res

    def __height(self, root):
        if not root.children:
            return 1

        return 1 + max([self.__height(child) for child in root.children])

    def height(self):
        return self.__height(self.__root) - 1

    def find(self, value):
        return self.__find(value)

    def add_child(self, parent, child):
        node = self.__find(parent)
        node.children.append(self.TreeNode(child))
        self.__size += 1

    def count_nodes(self):
        return self.__size

    def tree_levels_node(self):
        queue = deque()
        queue.append((0, self.__root))

        result = {}

        while len(queue) != 0:
            level, current_node = queue.popleft()

            if level not in result:
                result[level] = [current_node]
            else:
                result[level].append(current_node)

            for child in current_node.children:
                queue.append((level + 1, child))

        return result

    def tree_levels(self):
        queue = deque()
        queue.append((0, self.__root))

        result = {}

        while len(queue) != 0:
            level, current_node = queue.popleft()

            if level not in result:
                result[level] = [current_node.value]
            else:
                result[level].append(current_node.value)

            for child in current_node.children:
                queue.append((level + 1, child))

        return result

    def root_to_dst_leaf(self, node, dst, path):
        path.append(node.value)

        if node.value == dst:
            return path

        for child in node.children:
            child_path = self.root_to_dst_leaf(child, dst, path)
            if child_path:
                return child_path
            else:
                path.remove(child.value)


class Frog:

    def __init__(self, right, left):
        self.right = right
        self.left = left
        self.value = ""

    def set_frog(self):
        if self.right:
            self.value = ">"
        if self.left:
            self.value = "<"


class FrogNode:

    def __init__(self, string):
        self.string = string
        self.priority = 0
        self.children = []


class Rules:

    def __init__(self, string, u_idx):
        self.string = string
        self.u_idx = u_idx
        self.state = string

    def validator(self, idx):
        return bool(idx >= 0 and idx < len(self.state))

    def rule_one(self):
        if self.validator(self.u_idx - 1) is False:
            return "Error"
        self.string = self.state
        if self.string[self.u_idx - 1] == ">":
            self.string = list(self.string)
            self.string[self.u_idx - 1], self.string[self.u_idx] = \
                self.string[self.u_idx], self.string[self.u_idx - 1]
            self.string = ''.join(self.string)
        return self.string

    def rule_two(self):
        if self.validator(self.u_idx - 2) is False:
            return "Error"
        self.string = self.state
        if self.string[self.u_idx - 2] == ">":
            self.string = list(self.string)
            self.string[self.u_idx - 2], self.string[self.u_idx] = \
                self.string[self.u_idx], self.string[self.u_idx - 2]
            self.string = ''.join(self.string)
        return self.string

    def rule_three(self):
        if self.validator(self.u_idx + 1) is False:
            return "Error"
        self.string = self.state
        if self.string[self.u_idx + 1] == "<":
            self.string = list(self.string)
            self.string[self.u_idx + 1], self.string[self.u_idx] = \
                self.string[self.u_idx], self.string[self.u_idx + 1]
            self.string = ''.join(self.string)
        return self.string

    def rule_four(self):
        if self.validator(self.u_idx + 2) is False:
            return "Error"
        self.string = self.state
        if self.string[self.u_idx + 2] == "<":
            self.string = list(self.string)
            self.string[self.u_idx + 2], self.string[self.u_idx] = \
                self.string[self.u_idx], self.string[self.u_idx + 2]
            self.string = ''.join(self.string)
        return self.string


class FrogTree:
    # '>>>_<<<'
    def __init__(self, root_value):
        self.tree = Tree(root_value)
        self.combs = []
        self.global_combs = []
        self.all_combs = []
        self.level = 1

    def set_combs(self):
        self.combs = self.tree.tree_levels_node()[self.level]
        self.level += 1
        return self.level

    def get_root_combs(self, node):
        idx = 0
        for sym in range(0, len(list(node.value))):
            if list(node.value)[sym] == "_":
                idx = sym
        rules = Rules(node.value, idx)

        res = []
        if rules.rule_one() not in self.all_combs and \
           rules.rule_one() != "Error":
            res.append(rules.rule_one())

        if rules.rule_two() not in self.all_combs and \
           rules.rule_two() != "Error":
            res.append(rules.rule_two())

        if rules.rule_three() not in self.all_combs and \
           rules.rule_three() != "Error":
            res.append(rules.rule_three())

        if rules.rule_four() not in self.all_combs and \
           rules.rule_four() != "Error":
            res.append(rules.rule_four())

        for child in res:
            self.tree.add_child(node.value, child)

        self.all_combs += res

        return res

    def get_current_combs(self):
        return self.combs

    def get_next_combs(self):
        self.global_combs = self.combs
        res = []
        for node in self.global_combs:
            res += self.get_root_combs(node)
        return res

    def generate_all(self):
        self.get_root_combs(self.tree.root())
        self.set_combs()
        while len(self.get_next_combs()) != 1:
            self.get_next_combs()
            self.set_combs()


def main():
    frog = FrogTree(">>>_<<<")
    frog.generate_all()
    # print(frog.tree.tree_levels())
    # print(frog.tree.DFS(frog.tree.root()))
    print(frog.tree.root_to_dst_leaf(frog.tree.root(), '<<<_>>>', []))
    # print(frog.tree.all_root_to_leaf(frog.tree.root()))


if __name__ == '__main__':
    main()
