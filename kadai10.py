#kadai10
#うるう年判定
seireki = int(input())
uruu = 0

if seireki % 4 == 0:
    uruu = 1
    if seireki % 100 == 0:
        uruu = 0
        if seireki % 400 == 0:
            uruu = 1

if uruu == 1:
    print("Uruu doshi!")
else:
    print("Not Uruu doshi!")