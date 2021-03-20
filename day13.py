def read_input(name):
    with open(name,'r') as file:
        inp=[]
        inp.append(file.readline()[:-1])
        inp.append(file.readline().split(','))
        return inp


def mount_schedule(inp):
    time=int(inp[0])
    buses=inp[1]

    print(f'time  ', end='')
    for bus in buses:
        print(f'bus {bus:3s}',end='')
    print()
    
    for t in range(time-2, time+11):
        inStop=[]
        for bus in buses:
            if t%int(bus)==0:
                inStop.append("D")
            else:
                inStop.append(".")
        print(t, end='    ')
        for k in inStop:
            print(k,end='       ')
        print()

def pick_bus(inp):
    time=int(inp[0])
    buses=inp[1]
    t=time
    while(True):
        for bus in buses:
            if bus == 'x':
                continue
            elif t%int(bus)==0:
                return t, bus
                break
        t+=1


inp=read_input('day13.dat')
time=int(inp[0])
buses=inp[1]
# while True:
#     try:
#         inp[1].remove('x')
#     except ValueError:
#         break

# mount_schedule(inp)
t,bus=pick_bus(inp)
print((t-time)*int(bus))


def check_time(buses, time):
    # for num, id in enumerate(buses):
    # print(f'{time} {[(time+k)%int(buses[k])==0 for k in range(len(buses)) if buses[k]!="x"]}')
    check=[]
    for k in range(len(buses)):
        if buses[k]!='x':
            if (time+k)%int(buses[k])==0:
                check.append(True)
            else:
                return False
    return time
        
# t=0
# while(True):
#     check=check_time(buses,t)
#     if check:
#         print(check)
#         break
#     t+=1 

t=int(buses[0])
dt=int(buses[0])
for num, bus in enumerate(buses):
    print(f'1-{t} {dt} {num} {bus} ')
    if bus=='x':
        continue
    while((t+num)%int(bus)!=0):
        t+=dt
        if check_time(buses[0:num+1], t):
            print(f'2-{t} {dt} {num} {bus} ')
            dt*=int(bus)

