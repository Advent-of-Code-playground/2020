inp=[]
entry=0
while(True):
    entry=input()
    if entry=="":
        break
    inp.append(int(entry))


for i in range(len(inp)-2):
    for j in range(i, len(inp)-1):
        for k in range (j, len(inp)):
            a=inp[i]
            b=inp[j]
            c=inp[k]
            if (a+b+c==2020):
                print(a,b,c,c*a*b)
