people = "><<<<<><>><>><>><>><><><>><><<"

while True:
    print(people)
    people_new = people.replace("><", "<>")

    if people_new == people:
        print("OK")
        break

    people = people_new



# text = "abcdef"
# new_text = text.replace("c", "C")
# print(text)
# print(new_text)