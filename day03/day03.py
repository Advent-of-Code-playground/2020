


map=[]
while(True):
    inp=input()
    if inp=="":
        break
    else:
        map.append(inp)

currentPos=(0,0)
squares=0
trees=0

for k in range(0,len(map)+1,2):
    if currentPos[0] >= len(map[k]):
        newx=currentPos[0] - len(map[k])*( currentPos[0]//len(map[k])  )
        currentPos=(newx, currentPos[1])

    x=currentPos[0]
    y=currentPos[1]
    print(x,y)
    print(map[y][x])

    if map[y][x] == ".": squares+=1
    elif map[y][x] == "#": trees+=1

    currentPos=(x+1,y+2)

print(squares, trees)

