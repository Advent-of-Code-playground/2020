def read_inp(name):
    with open(name,'r') as input:
        inp='8'
        inpList=[]
        while(inp!=""):
            inp=input.readline()
            inpList.append(inp[:-1])
    inpList.pop()
    return inpList


inp=read_inp('day9.dat')

preamble=25
for pos, value in enumerate(inp):
    if pos < preamble:
        pass
    else:
        check=False
        for val1 in range(pos-preamble, pos-1):
            for val2 in range(val1, pos):
                n1=int(inp[val1])
                n2=int(inp[val2])
                if (n1+n2==int(value)):
                    check=True
        if not check:
            print(f'{pos}: {value}')
            break

for pos in range(len(inp)):
    sumList=[]
    for pos2 in range(pos, len(inp)):
        sumList.append(int(inp[pos2]))
        if sum(sumList) == int(value):
            top=max(sumList)
            bot=min(sumList)
            print(f'{value}: Max: {top}. Min: {bot}. Adding: {bot+top}')
        elif sum(sumList) > int(value):
            break
