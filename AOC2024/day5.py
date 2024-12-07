import re



# PART 1



itemsL = []
itemsR = []
addLis = []



with open('d5.txt','r+') as f:
    txt = f.read()



sec1 = str(re.findall('\d\d\|\d\d',txt))
txt = txt.split('\n')
sec2 = txt[1177:]



for line in sec2:
    lineLis = []
    line = line.split(',')
    for num in line:
        matchCnt = 0
        match = re.findall(f'{num}\|\d\d',sec1)
        inLis = 0
        for i in match:
            for numSearch in line:
                if i[-2:] == numSearch:
                    matchCnt += 1
        lineLis.append([matchCnt, num])
    addLis.append(lineLis)



sortLis = []
for lines in addLis:
    temp = []
    order = False
    for num in range(len(lines)):
        try:
            x = lines[num+1]
            if x < lines[num]:
                order = True
            else:
                order = False
        except IndexError:
            pass
        if order == False:
            break
    if order == True:
        for i in lines:
            temp.append(i[-1])
    sortLis.append(temp)



total = 0
sortLis = list(filter(None,sortLis))
for lines in list(sortLis):
    length = len(lines)
    total += int(lines[length//2])
    


print(total)



# PART 2



itemsL = []
itemsR = []
addLis = []



with open('d5.txt','r+') as f:
    txt = f.read()



sec1 = str(re.findall('\d\d\|\d\d',txt))
txt = txt.split('\n')
sec2 = txt[1177:]



for line in sec2:
    lineLis = []
    line = line.split(',')
    for num in line:
        matchCnt = 0
        match = re.findall(f'{num}\|\d\d',sec1)
        inLis = 0
        for i in match:
            for numSearch in line:
                if i[-2:] == numSearch:
                    matchCnt += 1
        lineLis.append([matchCnt, num])
    addLis.append(lineLis)



sortLis = []
for lines in addLis:
    temp = []
    order = False
    for num in range(len(lines)):
        try:
            x = lines[num+1]
            if x < lines[num]:
                order = True
            else:
                order = False
        except IndexError:
            pass
        if order == False:
            break
    if order == False:
        for i in lines:
            temp.append(i)
    sortLis.append(temp)



sortLis = list(filter(None,sortLis))
pt2sortLis = []
for line in sortLis:
    orderedLis = []
    for count in range(len(line)):
        for chunk in line:
            if int(chunk[0]) == count:
                orderedLis.append(int(chunk[-1]))
    pt2sortLis.append(orderedLis)



total = 0
for lines in pt2sortLis:
    length = len(lines)
    total += int(lines[length//2])



print(total)