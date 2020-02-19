def read_file(file_name: str) -> tuple:
    global n, pat
    fr = open(file_name, mode='r')
    text = fr.read()
    n, pat = text.strip().split('\n')
    n = int(n)
    fr.close()
    return n, pat


def write_file(file_name: str, pat: str, n: int):
    fw = open(file_name, mode='w')
    for i in range(n):
        for j in range(n):
            fw.write(pat)
        fw.write('\n')
    fw.close()


# number_of_lines, pattern = read_file("input.txt")
write_file("output.txt", pattern, number_of_lines)
