import glob


list_of_files = glob.glob('./files/*.txt')

child_to_parent = {}

for path in list_of_files:
    esme_file = path[8:18]

    with open(path) as f:
        matne_file = f.read()


    child_to_parent[esme_file] = matne_file

print(child_to_parent)
