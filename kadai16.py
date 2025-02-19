#kadai16
#バブルソート
l = [24,17,16,18]
for i in range(len(l)-1):
    for j in range((len(l)-1)-i):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp
print(l)