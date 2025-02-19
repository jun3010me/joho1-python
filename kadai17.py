#kadai17
#選択ソート
l = [24,17,16,18]
for i in range(len(l)-1):
    for j in range(i,(len(l)-1)):
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print(l)