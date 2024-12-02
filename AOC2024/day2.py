# PART 1



with open('d2.txt', 'r+') as f:
    x = f.readlines()



lis = []
safeCnt = 0



for i in x:
    lis.append(i.split(' '))



for i in lis:
    safe = True
    add = 0

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
    safe = True
    add = 0

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

    if safe == True:
        safeCnt += 1
        pass
    else:
        failLis.append(i)



lis.clear()
       
for i in failLis:
    temp = []
    for a in i:
        temp.append(int(a))
    lis.append(temp)
        















for i in lis:
    fails = 0
    iCopy = i.copy()
    for a in i:
        safe = True
        aPos = i.index(a)
        
        iCopy.remove(a)

        for j in range(len(iCopy)):

            try:
                iCopy[j+1]
            except IndexError:
                pass
            else:
                b = iCopy[j] - iCopy[j+1]

                if b > 3 or b < -3 or b == 0:
                    safe = False

                if b > 0:
                    add += 1

            if add + 1 != len(iCopy) and add != 0:
                safe = False

        if safe == False:
            fails += 1
            




        iCopy.insert(aPos, a)
        #print(aPt)


    if fails < 2:
        safeCnt += 1






print(safeCnt)
f.close()