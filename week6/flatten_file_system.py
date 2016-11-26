import os
from tree import Tree


class FileSystem:

    def __init__(self, root):
        self.file_system = Tree(root)
        self.level = []

    def add_root_dirs(self):
            for _dir in sorted(os.listdir('.')):
                self.file_system.add_child(self.file_system.root.value,
                                           os.path.abspath(_dir))
            self.level = self.file_system.root.children

    def add_next_level(self):
        while self.level != []:
            for child in self.level:
                if os.path.isdir(child.value):
                    os.chdir(child.value)
                    for c in os.listdir(child.value):
                        self.file_system.add_child(child.value,
                                                   os.path.realpath(c))
                os.chdir('..')
            self.level = [c for c in child.children for child in self.level]

    def flatten_file_system1(self):
        return self.flatten()

    def flatten(self):
        return [val for subxs in self.file_system.tree_levels()
                for val in subxs]

    def flatten_file_system2(self):
        return self.file_system.DFS(self.file_system.root)


def main():
    sys = FileSystem(os.path.abspath("."))
    sys.add_root_dirs()
    sys.add_next_level()
    print(sys.flatten_file_system2())


if __name__ == '__main__':
    main()
