def read_inp(name):
    with open(name,'r') as file:
        return file.readlines()

def eval_eq(eq):
    val=0
    return val

inp=read_inp('day18.dat')
print(inp)
for eq in inp:
    print(eval_eq(eq))