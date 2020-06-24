fname = "input.txt"

f = open("input.txt", mode="r+")
# text = f.read(5)
f.seek(5)
f.write("...")

f.seek(14)
f.write('...')


