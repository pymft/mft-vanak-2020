class Sample:
    number = 1000


s1 = Sample()
s2 = Sample()

print(s1.number, s2.number)

Sample.number = 999
s1.number = 1
print(s1.number, s2.number)