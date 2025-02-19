#kadai15
#素数判定
kazu = int(input("Please input any value =>"))
sosuu = 1
for i in range(2,kazu):
    if kazu%i==0:
        sosuu = 0
        break

if sosuu == 0:
    print("Not Sosuu")
else:
    print("Sosuu")