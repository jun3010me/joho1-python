#kadai9
#二分探索を行う
l = [11,24,36,42,58,63,77]
i = 0
j = 6
s = int(input())
count = 0
while i<=j:
    count+=1
    m = int((i + j)/2)
    if l[m]==s:
        print("Hakken!",count)
        break
    if l[m] < s:
        i = m + 1
    else:
        j = m - 1