
global check
global allBags

def search(bagList, originBag, bag):
    global check
    # print(originBag)
    # print(bagList[originBag])
    for innerBag in bagList[originBag]:
        if innerBag[1]==bag:
            check = True
        elif innerBag[1]=='no other':
            pass
        else:
            search(bagList, innerBag[1], bag)


def read_inp(name):
    bags={}
    with open(name, 'r') as file:
        while (True):
            inp=file.readline()
            if inp=="":
                break
            originBag=inp.split("contain")[0][:-6]
            if originBag in bags:
                print("It shouldn't be allowed")
                quit()
            bagList=[]
            for innerBag in inp.split("contain")[1].split(','):
                if 'no other' in innerBag:
                    n, bag = 0, 'no other'
                    bagList.append((n, bag))        
                else:
                    n = int(innerBag.split()[0])
                    bag = innerBag.split()[1]+" "+innerBag.split()[2]
                    bagList.append((n, bag))        
            bags[originBag]=bagList
    return bags

bags=read_inp("day7.dat")
validBags=[]
for key in bags:
    global check
    check = False
    search(bags, key, 'shiny gold')
    if check == True:
        validBags.append(key)
    
print(len(validBags))

#------------------//---------------#

def count_branch(bagList, n, originBag):
    ''' DEPRECATED'''
    global sum
    for innerBag in bagList[originBag]:
        if innerBag[1]=='no other':
            return n
        else:
            return n*count_branch(bags, innerBag[0], innerBag[1])

def count(bagList, n, originBag):
    global allBags
    for innerBag in bagList[originBag]:
        if innerBag[1]=='no other':
            pass
        else:
            allBags += n*innerBag[0]
            for k in range(n):
                count(bagList, innerBag[0], innerBag[1])
        

allBags=0
count(bags, 1, 'shiny gold')
print(allBags)


    
    
    
