#kadai13
#10進数から2進数に変換
jushin = int(input("Please input 10shinsu =>"))
keta = 1
nishin = 0
while jushin > 0:
    nishin += jushin%2*keta
    jushin//=2
    keta*=10
print(nishin)