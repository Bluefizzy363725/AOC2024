# PART 1



from tabnanny import check


with open('d2.txt', 'r+') as f:
    x = f.readlines()



lis = []
safeCnt = 0


def CheckSafe(i):
    safe=True
    add=0
    for a in range(len(i)):
        try:
            int(i[a+1])
        except IndexError:
            pass
        else:
            b = int(i[a]) - int(i[a+1])

            if b > 3 or b < -3 or b == 0:
                safe = False

            if b > 0:
                add += 1

    if add + 1 != len(i) and add != 0:
        safe = False

    return safe




for i in x:
    lis.append(i.split(' '))



for i in lis:
    safe = CheckSafe(i)
 

    if safe == True:
        safeCnt += 1



print(safeCnt)
f.close()



# PART 2



with open('d2.txt', 'r+') as f:
    x = f.readlines()



lis = []
failLis = []
safeCnt = 0
    


for i in x:
    lis.append(i.split(' '))
    


for i in lis:
    safe = CheckSafe(i)
 


    if safe == True:
        safeCnt += 1
    else:
        for a in range(len(i)):
            newi=i.copy()
            newi.pop(a)
            safe = CheckSafe(newi)
            if safe:
                safeCnt += 1
                break



print(safeCnt)
f.close()