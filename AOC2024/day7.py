# PART 1



with open('d7.txt','r+') as f:
    txt = f.readlines()
count = 0



for line in txt:
    line = line.split(' ')
    total = line[0][:-1]
    solved = False
    for space in range(2**(len(line[1:])-1)):
        lis = []
        sequence = bin(space)[2:].zfill(len(line[1:])-1)
        for num in range(len(sequence)):
            lis.append(line[num+1])
            if sequence[num] == '0':
                lis.append('+')
            else:
                lis.append('*')
        lis.append(line[-1])
        for i in range(len(lis)):
            if len(lis) == 1:
                if lis[0] == int(total):
                    count += int(lis[0])
                    solved = True
                break
            else:
                a = eval(str(lis[0])+str(lis[1])+str(lis[2]))
                lis = lis[2:]
                lis[0] = a
        if solved == True:
            break
            


print(count)



# PART 2



def toBase3(space):
    space = abs(space)
    if space < 3:
        return space
    num = ''
    while space != 0:
        num = str(space % 3) + num
        space = space // 3
    return num



with open('d7.txt','r+') as f:
    txt = f.readlines()
count = 0
passLis = []



for line in txt:
    line = line.split(' ')
    total = line[0][:-1]
    solved = False
    for space in range(3**(len(line[1:])-1)):
        lis = []
        sequence = str(toBase3(space)).zfill(len(line[1:])-1)
        for num in range(len(sequence)):
            lis.append(line[num+1])
            if sequence[num] == '0':
                lis.append('+')
            elif sequence[num] == '1':
                lis.append('||')
            else:
                lis.append('*')
        lis.append(line[-1])
        for i in range(len(lis)):
            if len(lis) == 1:
                if int(lis[0]) == int(total):
                    count += int(lis[0])
                    solved = True
                break
            else:
                if str(lis[1]) == '||':
                    a = str(lis[0]) + str(lis[2])
                else:
                    a = eval(str(lis[0])+str(lis[1])+str(lis[2]))
                lis = lis[2:]
                lis[0] = a
        if solved == True:
            print('SOLVED LINE')
            break




print(count)