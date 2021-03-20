def read_inp(name):
    with open(name,'r') as input:
        inpList=[]
        while(True):
            inp=input.readline()
            if inp=='':
                break
            inpList.append(int(inp[:-1]))
    return inpList
    

def count_diffs(path):
    d1=0
    d2=0
    d3=0
    for pos in range(1, len(testPath)):
        if testPath[pos]-testPath[pos-1] == 1:
            d1+=1
        elif testPath[pos]-testPath[pos-1] == 2:
            d2+=1
        elif testPath[pos]-testPath[pos-1] == 3:
            d3+=1
        else:
            return False, 0, 0, 0,
        # print(f'{sInp[pos]:3d}, {sInp[pos-1]:3d}, {d1:3d},{d2:3d},{d3:3d} ')
    
    d3+=1
    return True, d1,d2,d3

#

inp=read_inp('day10.dat')
sInp=sorted(inp)
print(sInp)

pcJolt=[0]
pcAdap=[max(sInp)+3]
testPath=pcJolt+sInp+pcAdap

splitedInp=[]
a=0
b=0
for k in range(1,len(testPath)):
    if testPath[k]-testPath[k-1]==3:
        b=k
        splitedInp.append(testPath[a:b])
        a=b
print(splitedInp)

mul=1
for split in splitedInp:
    if len(split)==5:
        mul*=7
    elif len(split)==3:
        mul*=2
    elif len(split)==4:
        mul*=4
    elif len(split)==1:
        pass
    elif len(split)==2:
        pass
    else:
        print('err')
        print(split)
        quit()
print(mul)

# check, d1,d2,d3=count_diffs(sInp)
# print(d1*d3)
