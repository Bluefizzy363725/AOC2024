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