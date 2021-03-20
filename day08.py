def read_inp(name):
    with open(name,'r') as input:
        inp='8'
        instructions=[]
        while(inp!=""):
            inp=input.readline()
            instructions.append((inp[:3],inp[4:-1]))
    instructions.pop()
    return instructions

acc=0
count=0
countList=[0]
instructions=read_inp('day8.dat')
while (count != len(instructions)):
    inst=instructions[count][0]
    op  =instructions[count][1]
    if inst == "nop":
        pass
    elif inst == "acc":
        acc+=int(op)
    elif inst == "jmp":
        count+=int(op)-1
    count+=1
    if count in countList:
        print("Break!: ", acc, count)
        break
    countList.append(count)
    print(acc, count, instructions[count])

#---------------//--------------#

def test(instructions):
    acc=0
    count=0
    countList=[0]
    while (count != len(instructions)):
        inst=instructions[count][0]
        op  =instructions[count][1]
        if inst == "nop":
            pass
        elif inst == "acc":
            acc+=int(op)
        elif inst == "jmp":
            count+=int(op)-1
        count+=1
        if count in countList:
            print("Break!: ", acc, count)
            return False
        countList.append(count)
    return True


# for count in range(len(instructions)):
#     currentInst=instructions[:]
#     inst=instructions[count][0]
#     op  =instructions[count][1]
#     # print(instructions[count])
#     if inst == "jmp":
#         currentInst[count]=('nop',op)
#     elif inst == "nop":
#         currentInst[count]=('jmp',op)

#     if (test(currentInst)):
#         print(count)
#         break