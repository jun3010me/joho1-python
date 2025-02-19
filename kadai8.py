#kadai8
#1から入力した数値までの、偶数の総和を求める
n = int(input())
goukei = 0
for n in range(n+1):
    if n % 2 == 0:
        goukei += n
print(goukei)