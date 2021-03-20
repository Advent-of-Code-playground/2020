import numpy as np

def read_input(name):
    with open(name,'r') as file:
        inp=[]
        for line in file:
            inp.append(line[:-1])
        return inp

inp=read_input('day12.dat')
print(inp)

def execute_instruction_1(pos, inst):
    ord=inst[0]
    op=int(inst[1:])
    
    if ord == "F":
        da=0
        dx=op*np.sin(pos[0]*np.pi/180)
        dy=op*np.cos(pos[0]*np.pi/180)
    elif ord == "R":
        da=op
        dx=0
        dy=0
    elif ord == "L":
        da=-op
        dx=0
        dy=0
    elif ord == "N":
        da=0
        dx=0
        dy=+op
    elif ord == "S":
        da=0
        dx=0
        dy=-op
    elif ord == "E":
        da=0
        dx=+op
        dy=0
    elif ord == "W":
        da=0
        dx=-op
        dy=0
    else:
        print(f'Incorrect instructions')

    na=pos[0]+da
    nx=pos[1]+dx
    ny=pos[2]+dy
    pos=[na,nx,ny]

    return pos


def execute_instruction_2(pos, wayP, inst):
    ord=inst[0]
    op=int(inst[1:])
    
    movePos=False
    moveWayP=False

    if ord == "F":
        dist=np.sqrt( (wayP[1]-pos[1])*(wayP[1]-pos[1]) + (wayP[2]-pos[2])*(wayP[2]-pos[2]) )
        dirx=(wayP[1]-pos[1])/dist
        diry=(wayP[2]-pos[2])/dist

        dirx=1
        diry=1

        dx=op*wayP[1]*dirx
        dy=op*wayP[2]*diry
        movePos=True
    elif ord == "R":
        # dx=wayP[1]-pos[1]
        # dy=wayP[2]-pos[2]
        op=-op*np.pi/180
        x=wayP[1]
        y=wayP[2]
        dx=x*np.cos(op)-y*np.sin(op)-x
        dy=y*np.cos(op)+x*np.sin(op)-y
        moveWayP=True
    elif ord == "L":
        op=op*np.pi/180
        # dx=wayP[1]-pos[1]
        # dy=wayP[2]-pos[2]
        x=wayP[1]
        y=wayP[2]
        dx=x*np.cos(op)-y*np.sin(op)-x
        dy=y*np.cos(op)+x*np.sin(op)-y
        moveWayP=True
    elif ord == "N":
        dx=0
        dy=+op
        moveWayP=True
    elif ord == "S":
        dx=0
        dy=-op
        moveWayP=True
    elif ord == "E":
        dx=+op
        dy=0
        moveWayP=True
    elif ord == "W":
        dx=-op
        dy=0
        moveWayP=True
    else:
        print(f'Incorrect instructions')

    if movePos:
        na=pos[0]
        nx=pos[1]+dx
        ny=pos[2]+dy
        pos=[na,nx,ny]
    elif moveWayP:
        na=wayP[0]
        nx=wayP[1]+dx
        ny=wayP[2]+dy
        wayP=[na,nx,ny]
    
    return pos, wayP


# pos = [ang, x, y]
pos=[0,0,0]
wayP=[0,10,1]
for inst in inp:
    # pos=execute_instruction_1(pos, inst)
    pos, wayP=execute_instruction_2(pos, wayP, inst)
    print(inst)
    print(pos, wayP)

print(abs(pos[1])+abs(pos[2]))