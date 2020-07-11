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
        value.add_child(self)

    @property
    def children_count(self):
        return len(self.children)



a = Node('1000')
b = Node('2000')
c = Node('3000')
d = Node('1000')
e = Node('5000')

b.parent = a
c.parent = a
e.parent = b

print(b.parent)
print(d.children, d.children_count)
print(b.children, b.children_count)

for node in Node.instances.values():
    print(node)


#
# Node.read_all_files('./files', 'txt')
# no_children = Node.no_children_nodes()
#
# for node in no_children:
#     print(node.ancestors)
