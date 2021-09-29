# Author: Yongdong Xi (Sep 28 2021)

Card1 = int(input("wha is the point of the first card?"))
Card2 = int(input("wha is the point of the second card?"))

if Card1 + Card2 <= 21:
    print("you are safe")
else:
    print("you are busted")
