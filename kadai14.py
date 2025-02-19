#kadai14
#2進数から10進数に変換
nishin = int(input("Please input 2shinsu =>"))
keta = 1
jushin = 0
while nishin > 0:
    jushin += nishin%10*keta
    nishin//=10
    keta*=2
print(jushin)