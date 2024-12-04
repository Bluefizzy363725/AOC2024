# PART 1



with open('d4.txt', 'r+') as f:
    txt = f.readlines()



count = 0



for y in range(len(txt)):
    for x in range(len(txt[y])):

        try: 
            a = f'{txt[y][x]}{txt[y+1][x]}{txt[y+2][x]}{txt[y+3][x]}'
            if a == 'XMAS':
                count += 1
        except IndexError:
            pass

        try: 
            a = f'{txt[y][x]}{txt[y+1][x+1]}{txt[y+2][x+2]}{txt[y+3][x+3]}'
            if a == 'XMAS':
                count += 1
        except IndexError:
            pass

        try: 
            a = f'{txt[y][x]}{txt[y][x+1]}{txt[y][x+2]}{txt[y][x+3]}'
            if a == 'XMAS':
                count += 1
        except IndexError:
            pass
            
        try: 
            a = f'{txt[y][x]}{txt[y-1][x+1]}{txt[y-2][x+2]}{txt[y-3][x+3]}'
            
            if a == 'XMAS' and y-3 >= 0:
                count += 1
        except IndexError:
            pass

        try: 
            a = f'{txt[y][x]}{txt[y-1][x]}{txt[y-2][x]}{txt[y-3][x]}'
            if a == 'XMAS' and y-3 >= 0:
                count += 1
        except IndexError:
            pass

        try: 
            a = f'{txt[y][x]}{txt[y-1][x-1]}{txt[y-2][x-2]}{txt[y-3][x-3]}'
            if a == 'XMAS' and y-3 >= 0 and x-3 >= 0:
                count += 1
        except IndexError:
            pass

        try: 
            a = f'{txt[y][x]}{txt[y][x-1]}{txt[y][x-2]}{txt[y][x-3]}'
            if a == 'XMAS' and x-3 >= 0:
                count += 1
        except IndexError:
            pass

        try: 
            a = f'{txt[y][x]}{txt[y+1][x-1]}{txt[y+2][x-2]}{txt[y+3][x-3]}'
            if a == 'XMAS' and x-3 >= 0:
                count += 1
        except IndexError:
            pass



print(count)
f.close()



# PART 2



with open('d4.txt', 'r+') as f:
    txt = f.readlines()



count = 0



for y1 in range(len(txt)-2):
    for x1 in range(len(txt[y])-2):

        x=x1+1
        y=y1+1

        if txt[y][x] == 'A':
            r1 = 'MMSS'
            r2 = 'SMMS'
            r3 = 'SSMM'
            r4 = 'MSSM'
            
            try:
               a = f'{txt[y-1][x-1]}{txt[y-1][x+1]}{txt[y+1][x+1]}{txt[y+1][x-1]}'
            except IndexError:
                pass
            else:
                if (a == r1 or a == r2 or a == r3 or a == r4):
                    count += 1



print(count)
f.close