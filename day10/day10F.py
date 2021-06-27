def read_inp(name):
    with open(name,'r') as input:
        inpList=[]
        while(True):
            inp=input.readline()
            if inp=='':
                break
            inpList.append(int(inp[:-1]))
    return inpList
    

def count_diffs(testPath):
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

inp=read_inp('day10.dat')
sInp=sorted(inp)
# print(sInp)

check, d1,d2,d3=count_diffs(sInp)
print(d1*d3)

#####

def test_subList(subList):
    count=0
    if len(subList) == 1:
        return 1
    if len(subList) == 2:
        return 1
    for buffer in range(2**(len(subList)-2)):
        testSubList=subList[:]
        toRemove=f'0{bin(buffer)[2:]:>0{len(testSubList)-2}}0'
        for b in range(len(toRemove)):
            if toRemove[b]=='1':
                testSubList[b]='@'
        for _ in range(testSubList.count("@")):
            testSubList.remove('@')

        check, d1,d2,d3=count_diffs(testSubList)
        if check:
            print(f'{toRemove}, {testSubList}, {len(testSubList)}')
            count+=1
    return count
        

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

mul=1
for subList in splitedInp:
    count=test_subList(subList)
    mul*=count
    print(f'{subList} {count} {mul}')

print(mul)

