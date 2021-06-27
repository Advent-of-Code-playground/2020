n=3
grid=[]
for x in range(n):
    gridY=[]
    for y in range(n):
        gridZ=[]
        for z in range(n):
            gridZ.append('.')
        gridY.append(gridZ)
    grid.append(gridY)

with open('day17.dat','r') as file:
    inp=file.readlines()
print(inp)