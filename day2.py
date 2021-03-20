valid=0
while(True):
    entry=input()
    if entry=="":
        break
    else:
        inp=entry.split()
        lowerPos=int(inp[0].split('-')[0])
        higherPos=int(inp[0].split('-')[1])
        restraint=inp[1][0]
        password=inp[2]
        if password[lowerPos-1]==restraint:
            if password[higherPos-1]!=restraint:
                valid+=1
        elif password[higherPos-1]==restraint:
            valid+=1
        else:
            print(inp)

print(valid)

