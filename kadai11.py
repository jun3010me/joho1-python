#kadai11
#ユークリッドの互除法
dai = int(input("大きな数を入れてちょ"))
sho = int(input("小さな数を入れてちょ"))

while dai % sho != 0:
    amari = dai % sho
    dai = sho
    sho = amari
print(sho)