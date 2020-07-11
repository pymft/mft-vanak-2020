import glob


def get_child_to_parent(directory, extention):
    # files_path = directory + '/*.' + extention
    files_path = f"{directory}/*.{extention}"
    list_of_files = glob.glob(files_path)
    child_to_parent = {}

    start = len(directory) + 1
    stop = len(extention) + 1

    for path in list_of_files:
        child = path[start:-stop]
        with open(path) as f:
            parent = f.read()

        child_to_parent[child] = parent

    return child_to_parent


def get_nodes_with_no_parent(c2p):
    lst = []

    for k in c2p:
        if c2p[k] == '0':
            lst.append(k)
    return lst


def get_parent_to_children(p2c):
    out = {}

    for k, v in p2c.items():
        if k not in out:
            out[k] = []

        if v not in out:
            out[v] = []

        out[v].append(k)

    return out


def get_nodes_with_no_children(out):
    lst = []

    for k in out:
        if out[k] == []:
            lst.append(k)
    return lst


def ancestors(c2p, node_number):
    res = []
    while True:
        res.append(node_number)
        node_number = c2p[node_number]
        if node_number == '0':
            break

    res.append(node_number)
    return res



c2p = get_child_to_parent('./files_files_everywhere', 'txt')
print(c2p)
no_parent = get_nodes_with_no_parent(c2p)
print(no_parent)
p2c = get_parent_to_children(c2p)
print(p2c)
no_child = get_nodes_with_no_children(p2c)
print(no_child)

for i in no_child:
    print("***", ancestors(c2p, i))