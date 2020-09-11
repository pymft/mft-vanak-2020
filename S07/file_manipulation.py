# open(r"C:\Users\User\Desktop\Videos\hello.txt")
# f = open("C:\\Users\\User\\Desktop\\Videos\\hello.txt")
# f = open("C:/Users/User/Desktop/Videos/hello.txt")

# r"C:\Users\User\PycharmProjects\mft-vanak-2020\S07"
# r"C:\Users\User\PycharmProjects\mft-vanak-2020\S07\..\..\..\Desktop\Videos\hello.txt"
# r"..\..\..\Desktop\Videos\hello.txt"
# r"C:\Users\User\Desktop\Videos\hello.txt"


f = open(r"../../../Desktop/Videos/hello.txt", mode="a")

f.write("hello\n")

f.close()