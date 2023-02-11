#kadai3
#数値を入力し、数値が30未満であれば1、数値が30以上50未満であれば2、数値が50以上なら3を出力する
tokuten = int(input())
if tokuten < 30:
    g = 1
elif tokuten < 50:
    g = 2
else:
    g = 3
print(g)