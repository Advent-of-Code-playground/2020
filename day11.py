import os
import copy

def read_input(name):
    with open(name,'r') as file:
        inp=[]
        for line in file:
            inp.append([k for k in line if k != '\n'])
        return inp

def show_frame(n, frame):
    os.system('clear')
    print(f'Frame: {n}')
    for k in frame:
        print(f'{k[:]}')

def count_occ(inp,nl,nc):
    count=0
    for lines in range(nl-1, nl+2):
        for columns in range(nc-1, nc+2):
            if lines<0 or columns<0:
                continue
            if lines==nl and columns==nc:
                continue
            try:
                if inp[lines][columns]=="#":
                    count+=1
            except IndexError:
                pass
    return count

def get_floor_dir(inp, fnl, fnc, Lnl, Lnc):
    changeY=fnl-Lnl
    changeX=fnc-Lnc
    return (changeX, changeY)
    

def count_occ_space(inp,nl,nc):
    count=0
    for lines in range(nl-1, nl+2):
        for columns in range(nc-1, nc+2):
            if lines<0 or columns<0:
                continue
            if lines==nl and columns==nc:
                continue
            try:
                if inp[lines][columns]=="#":
                    count+=1
                elif inp[lines][columns]==".":
                    dx,dy=0,0
                    while (inp[lines+dy][columns+dx]=="."):
                        (ndx, ndy) = get_floor_dir(inp, lines+dy, columns+dx, nl, nc)
                        dx=ndx
                        dy=ndy
                        if (lines+dy)<0 or (columns+dx)<0:
                            break
                        if inp[lines+dy][columns+dx]=="#":
                            count+=1
                        elif inp[lines+dy][columns+dx]=="L":
                            continue
                        # else:
                        #     print(f"ERROR, {lines} {columns} {lines+dy} {columns+dx}{inp[lines+dy][columns+dx]}")

            except IndexError:
                pass
    return count

    
def show_occ(inp):
    countInp=copy.deepcopy(inp)
    for nl, line in enumerate(inp):
        for nc, column in enumerate(line):
            count=count_occ_space(inp,nl,nc)
            if countInp[nl][nc]!=".": 
                countInp[nl][nc]=str(count)
    show_frame('k',countInp)

def apply_rules(inp):
    newInp=copy.deepcopy(inp)
    for nl, line in enumerate(inp):
        for nc, column in enumerate(line):
            if column == "L":
                count=count_occ_space(inp,nl,nc)
                if count==0:
                    newInp[nl][nc]="#"
            elif column == "#":
                count=count_occ_space(inp,nl,nc)
                # if count>=4:
                if count>=5:
                    newInp[nl][nc]="L"
            elif column == ".":
                pass
            else:
                print(column)
                print("ERRO")
                quit()
    return newInp

frame=0
inp=read_input('day11.dat')
show_frame(frame, inp)
# show_occ(inp)

frame+=1
newInp=apply_rules(inp)
show_frame(frame, newInp)
# show_occ(newInp)

while(newInp!=inp):
    inp=newInp
    frame+=1
    newInp=apply_rules(inp)
    show_frame(frame, newInp)
    # show_occ(newInp)

count=0
for line in newInp:
    count+=line.count('#')
print(count)