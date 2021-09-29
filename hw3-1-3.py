# Author: Yongdong Xi (Sep 28 2021)

a = int(input("what is number a"))

x = a % 2
y = a % 3
z = a % 5

if x + y + z == 0:
    print(a, "is a multiple of 2, 3, or 5")
else:
    print(a, "is not a multiple of 2, 3, or 5")
