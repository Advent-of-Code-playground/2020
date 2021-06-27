def calc_id(row,col):
    return (row*8 + col)
        
def decode_row(inp):
    if len(inp)!=7:
        print("ERROR!a")
        quit()
    lRange=0
    hRange=127
    print(lRange, hRange)
    for k in inp:
        if k == "F":
            hRange=lRange + (hRange-lRange)//2
        elif k == "B":
            lRange=lRange + (hRange-lRange)//2 +1
        else:
            print("ERROR!b")
            quit()
    if k == "F": return lRange
    if k == "B": return hRange
    

def decode_col(inp):
    print(inp)
    if len(inp)!=3:
        print("ERROR!c")
        quit()
    lRange=0
    hRange=7
    print(lRange, hRange)
    for k in inp:
        if k == "L":
            hRange=lRange + (hRange-lRange)//2
        elif k == "R":
            lRange=lRange + (hRange-lRange)//2 +1
        else:
            print("ERROR!d")
            quit()
    if k == "R": return lRange
    if k == "L": return hRange
        
        
max=0
seats={}
while(True):
    inp=input()
    if inp=="":
        break
    row=decode_row(inp[0:7])
    col=decode_col(inp[7:10])
    if str(col) not in seats:
        seats[str(col)]=[]
    seats[str(col)].append(row)
    sid=calc_id(row,col)
    if sid > max: max=sid
    
print(max)
for k in sorted(seats):
    print(k, len(seats[k])) #sorted(seats[k]))
    print(k, sorted(seats[k]))
    
