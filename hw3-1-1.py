# Author: Yongdong Xi (Sep 28 2021)

Awin = int(input("How many games does team A win?"))
Atie = int(input("How many games does team A tie?"))
Bwin = int(input("How many games does team B win?"))
Btie = int(input("How many games does team B tie?"))

AScore = 3 * Awin + 1 * Atie
BScore = 3 * Bwin + 1 * Btie

if AScore > BScore:
    print("Team A has more points than Team B")
else:
    print("Team B has more points than Team A")
