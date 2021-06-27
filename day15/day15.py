inp=[0,3,6]

turn=len(inp)

# Brute Forcing
# while(turn<=30000000):
#     turn+=1
#     last=inp[-1]
#     if last not in inp[:-1]:
#         inp.append(0)
#     else:
#         inp.reverse()
#         lastTurn1=len(inp)-inp.index(last)
#         lastTurn2=len(inp)-inp.index(last,len(inp)-lastTurn1+1)
#         inp.reverse()
#         inp.append(lastTurn1-lastTurn2)
#     print(f'{turn} {inp[turn-1]}')


hist={}
for turn, val in enumerate(inp):
    hist[val]=0
turn+=1

while(turn<=10):
    turn+=1
    if val not in hist:
        val=0
        hist[val]=turn
        val=0
    else:
        val=(turn-1)-hist[val]
        hist[val]=turn+1

    print(f'{turn+1} {hist[val]}')
    turn+=1


