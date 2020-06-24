with open('./input.txt') as f:
    text = f.read()
    numbers = text.strip().split("\n")
    print(numbers)


new_numbers = [int(i)**2 for i in numbers]

with open('./output.txt', 'w') as f:
    for i in new_numbers:
        f.write(str(i))
        f.write('\n')
