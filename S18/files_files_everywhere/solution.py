import glob


class Node:
    instances = {}

    def __new__(cls, number: str):
        if number not in cls.instances:
            cls.instances[number] = super().__new__(cls)
            cls.instances[number].is_initialized = False

        return cls.instances[number]

    def __init__(self, number: str):
        if not self.is_initialized:
            self.number = number
            self.__parent = None
            self.__children = []
            self.is_initialized = True

    def __repr__(self):
        # return str(self.number)
        return f"Node({self.number})"

    @property
    def children(self):
        return self.__children

    def add_child(self, child):
        self.__children.append(child)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        self.__parent = value
        self.__parent.add_child(self)

    @property
    def children_count(self):
        return len(self.children)

    @property
    def ancestors(self):
        if self.parent is None:
            return [self]
        return self.parent.ancestors + [self]

    @classmethod
    def no_children_nodes(cls):
        no_children = []
        for node in cls.instances.values():

            if node.children_count == 0:
                no_children.append(node)

        return no_children

directory = "./files"
extension = "txt"

files_path = f"{directory}/*.{extension}"
list_of_files = glob.glob(files_path)
start = len(directory) + 1
stop = len(extension) + 1

for path in list_of_files:
    child_name = path[start:-stop]
    with open(path) as f:
        parent_name = f.read()


    Node(child_name).parent = Node(parent_name)


# print(Node.instances)
# print(Node('3339551577').ancestors)
# print(Node('0').children)

for node in Node.no_children_nodes():
    print(node.ancestors)

