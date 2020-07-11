import glob


class Node:
    instances = {}

    def __new__(cls, number):
        if number not in cls.instances:
            cls.instances[number] = super().__new__(cls)
            cls.instances[number].initialized = False
        return cls.instances[number]

    def __init__(self, number):
        if not self.initialized:
            self.number = number
            self.__parent = None
            self.__children = []
            self.initialized = True

    def __repr__(self):
        return f"{self.number}"

    def add_child(self, child):
        self.__children.append(child)

    @property
    def children(self):
        return self.__children

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        if not isinstance(value, Node):
            value = Node(value)

        self.__parent = value
        self.parent.add_child(self)

    @property
    def ancestors(self):
        if self.number == '0':
            return []

        return self.parent.ancestors + [self.parent]

    @property
    def has_no_children(self):
        return len(self.__children) == 0

    @classmethod
    def read_all_files(cls, directory, extension):
        files_path = f"{directory}/*.{extension}"
        list_of_files = glob.glob(files_path)
        child_to_parent = {}

        start = len(directory) + 1
        stop = len(extension) + 1

        for path in list_of_files:
            child_name = path[start:-stop]
            with open(path) as f:
                parent_name = f.read()

            child = Node(child_name)
            child.parent = parent_name

    @classmethod
    def no_children_nodes(cls):
        result = []
        for node in cls.instances.values():
            if node.has_no_children:
                result.append(node)

        return result


if __name__ == '__main__':
    Node.read_all_files('./files', 'txt')
    no_children = Node.no_children_nodes()

    for i, node in enumerate(no_children):
        print(i, node.ancestors)
