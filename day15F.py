inp=[0,3,1,6,7,5]

turn=len(inp)

# Brute Forcing
while(turn<=30000000):
    turn+=1
    last=inp[-1]
    if last not in inp[:-1]:
        inp.append(0)
    else:
        inp.reverse()
        lastTurn1=len(inp)-inp.index(last)
        lastTurn2=len(inp)-inp.index(last,len(inp)-lastTurn1+1)
        inp.reverse()
        inp.append(lastTurn1-lastTurn2)
    print(f'{turn} {inp[turn-1]}')


