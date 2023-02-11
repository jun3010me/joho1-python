#kadai17
#2から入力した数までの素数をリストアップする
max = int(input())
kazu = []
count = 0
for i in range(max):
    kazu.append(i + 1)
for i in range(2,max):
    for j in range(2,max):
        try:
            kazu.remove(i*j)
            count+=1
        except ValueError:
            pass
kazu.remove(1)
print(kazu)
print(count)