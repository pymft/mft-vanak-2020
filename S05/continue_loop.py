counter = 1

while True:
    counter += 1

    if counter % 2 == 0:
        continue

    if counter > 100:
        break

    print(counter)
    # counter = counter + 1
