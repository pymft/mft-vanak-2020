a = 1
n = 54
aaa = range(a, n+1)

lst = list(aaa)
print(lst)
print(len(lst))
len(lst) % 2 == 1
abc1 = lst[0:int(len(lst) / 2)]
abc2 = lst[int(len(lst) / 2)-1::-1]
abc = abc1 + abc2
print(abc)





