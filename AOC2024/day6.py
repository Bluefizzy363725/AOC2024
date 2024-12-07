import re
import os
import time



# PART 1



end = False
starLis = []
count = 1



with open('d6.txt','r+') as f:
    txt = f.readlines()



def colliders(collision, movePos):
    if txt[movePos[0]][movePos[-1]] == '#':
        collision = 1
    elif movePos[-1] < 0 or movePos[-1] > 129:
        collision = 2
    return collision



def positionFind(txt):
    for i in txt:
        a = re.search('[\^|\<|\>|v]',i)
        line = txt.index(i)
        if a != None:
            break
    a = int(list(a.span())[-1])-1
    guardPos = [line, a]

    return guardPos



def move(guardPos):
    collision = 0
    end = False
    x = guardPos[0] # Lines
    y = guardPos[-1] # Characters
    match txt[x][y]:
        case '^':
            movePos = [x-1, y]
            collision = colliders(collision, movePos)
            if collision == 1:
                txt[x] = re.sub('[\^]','>',txt[x])
            elif collision == 2:
                end = True
            else:
                txt[x] = re.sub('[\^]','*',txt[x])
                txt[x-1] = f'{txt[x-1][:y]}^{txt[x-1][y+1:]}'
        case 'v':
            movePos = [x+1, len(txt[x]), y]
            collision = colliders(collision, movePos)
            if collision == 1:
                txt[x] = re.sub('[v]','<',txt[x])
            elif collision == 2:
                end = True
            else:
                txt[x] = re.sub('[v]','*',txt[x])
                txt[x+1] = f'{txt[x+1][:y]}v{txt[x+1][y+1:]}'
        case '<':
            movePos = [x, y-1]
            collision = colliders(collision, movePos)
            if collision == 1:
                txt[x] = re.sub('[<]','^',txt[x])
            elif collision == 2:
                end = True
            else:
                txt[x] = re.sub('[\.|\*][<]','<*',txt[x])
        case '>':
            movePos = [x, y+1]
            collision = colliders(collision, movePos)
            if collision == 1:
                txt[x] = re.sub('[>]','v',txt[x])
            elif collision == 2:
                end = True
            else:
                txt[x] = re.sub('[>][\.|\*]','*>',txt[x])
    return end



while end == False:
    try:
        guardPos = positionFind(txt)
        end = move(guardPos)
    except IndexError:
        break



    '''

    # TO SIMULATE IT

    os.system('cls')
    for i in txt:
        print(i)
    '''



for i in txt:
    temp = re.findall('[\*]',i)
    starLis.append(temp)
starLis = filter(None,starLis)
for i in starLis:
    count += len(i)



print(count)