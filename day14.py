import copy

def read_input(name):
    with open(name,'r') as file:
        inp=[]
        for line in file:
            inp.append(line[:-1].split(' = '))
        return inp

def apply_inst_1(memory, mem, mask, operand):
    alloc=''
    for bit, val in enumerate(mask):
        if val=='X':
            alloc+=operand[bit]
        elif val=='1':
            alloc+='1'
        elif val=='0':
            alloc+='0'
    memory[mem]=alloc
    return memory

def apply_inst_2(memory, mem, mask, operand):
    alloc=operand
    memMask=''
    for bit, val in enumerate(mask):
        if val=='X':
            memMask+='X'
        elif val=='1':
            memMask+='1'
        elif val=='0':
            memMask+=mem[bit]
    
    countX=memMask.count("X")
    for poss in range(2**countX):
        possMask=f'{bin(poss)[2:]:0>{countX}}'
        newMemMask=copy.deepcopy(memMask)
        for x in range(countX):
            newMemMask=newMemMask.replace('X',possMask[x],1)
        memory[newMemMask]=alloc

    return memory


inp=read_input('day14.dat')
# print(inp)

memory={}

for inst, operand in inp:
    if 'mask' in inst:
        mask=operand
    elif 'mem' in inst:
        mem=f'{bin(int(inst[4:-1]))[2:]:>0{len(mask)}}'
        operand=f'{bin(int(operand))[2:]:>0{len(mask)}}'
        # memory=apply_inst_1(memory, mem, mask, operand)
        memory=apply_inst_2(memory, mem, mask, operand)

sum=0
for entry in memory.values():
    sum+=int(entry,2)
print(sum)

