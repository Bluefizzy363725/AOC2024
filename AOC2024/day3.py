# PART 1



import re
total = 0



with open('d3.txt', 'r+') as f:
    text = f.read()



x = re.findall("mul\([0-9]+,[0-9]+\)", text)



for i in x:
    i = i.lstrip('mul')
    i = i.strip('()')
    i = i.split(',')
    j = int(i[0])*int(i[1])
    total += j
  
    

print(total)



# PART 2



import re
total = 0
x = []



with open('d3.txt', 'r+') as f:
    text = f.read()



splitLis = re.split('do\(\)|don\'t\(\)', text)
order = re.findall('do\(\)|don\'t\(\)', text)
muls =  re.findall("mul\([0-9]+,[0-9]+\)", splitLis[0])
x.append(muls)



for i in range(len(splitLis)):
    try:
        order[i]
    except:
        break
    else:
        if order[i] == 'do()':
            muls =  re.findall("mul\([0-9]+,[0-9]+\)", splitLis[i+1])
            x.append(muls)
            


for i in x:
    for a in i:
        a = a.lstrip('mul')
        a = a.strip('()')
        a = a.split(',')
        b = int(a[0])*int(a[-1])
        total += b



print(total)