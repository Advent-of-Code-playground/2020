
group={}
count=0
answers=[]
allYes=[]
while(True):
    inp=input()
    if inp=="":
        count+=1
        group[count]=(answers, allYes)
        answers=[]
    elif inp=="!":
        break
    else:
        answers.append(inp)
        for ans in inp:
            if ans not in allYes:
                allYes.append(ans)



print(group)

sum=0
for key in group:
    for ans in group[key][1]:
        if all([ans in key for key in group[key][0]]):
            sum+=1
    
    
print(sum)
