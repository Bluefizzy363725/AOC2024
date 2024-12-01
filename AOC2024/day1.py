# PART 1



with open('d1.txt','r+') as f:
    x = f.readlines()



lis = []
lis1 = []
lis2 = []
total = 0



for i in x:
    lis.append(i)

for i in lis:
    lis1.append(int(i[0:5]))

for i in lis:
    lis2.append(int(i[-6:]))



while True:
    lis1smol = lis1[0]
    for i in lis1:
        if int(i) < int(lis1smol):
            lis1smol = i
    lis1.remove(lis1smol)

    lis2smol = lis2[0]
    for i in lis2:
        if int(i) < int(lis2smol):
            lis2smol = i
    lis2.remove(lis2smol)

    if lis1smol > lis2smol:
        total += (lis1smol-lis2smol)
    else:
        total += (lis2smol-lis1smol)

    if len(lis1) == 0 or len(lis2) == 0:
        break



print(total)
f.close()



#PART 2



with open('d1.txt','r+') as f:
    x = f.readlines()



lis = []
lis1 = []
lis2 = []
total = 0



for i in x:
    lis.append(i)

for i in lis:
    lis1.append(int(i[0:5]))

for i in lis:
    lis2.append(int(i[-6:]))



for i in lis1:
    temp = 0
    for a in lis2:
        if a == i:
            temp += 1
    total += (i * temp)



print(total)
f.close()