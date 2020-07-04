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


result = get_child_to_parent('./files', 'txt')
print(result)
