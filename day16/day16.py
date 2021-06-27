def read_input(name):
    with open(name,'r') as file:
        rules=[]
        yourTicket=[]
        tickets=[]

        line=file.readline()
        while(line!="\n"):
            rules.append(line[:-1])
            line=file.readline()
        
        line=file.readline()
        while(line!="\n"):
            yourTicket.append(line[:-1])
            line=file.readline()

        line=file.readline()
        while(line!="\n"):
            tickets.append(line[:-1])
            line=file.readline()

        return rules, yourTicket, tickets

def process_rules(rules):
    processedRules={}
    for rule in rules:
        name=rule.split(':')[0]
        range1=rule.split(':')[1].split(' or ')[0].strip()
        range2=rule.split(':')[1].split(' or ')[1].strip()
        processedRules[name]=(range1, range2)
    return processedRules

def process_tickets(tickets):
    processedTickets=[]
    for num, ticket in enumerate(tickets):
        if num == 0:
            continue
        processedTickets.append(ticket.split(','))
    return processedTickets

def check_entry(entry, rule):
    rule1=rule[0]
    rule2=rule[1]
    checkL1=int(entry)>=int(rule1.split('-')[0])
    checkH1=int(entry)<=int(rule1.split('-')[1])
    checkL2=int(entry)>=int(rule2.split('-')[0])
    checkH2=int(entry)<=int(rule2.split('-')[1])
    if (checkL1 and checkH1) or (checkL2 and checkH2):
        return(True)
    else:
        return(False)

def check_ticket(ticket, rules):
    checkAll=[]
    getWrongs=[]
    for entry in ticket:
        checkEntry=[]
        for rule in rules:
            checkEntry.append(check_entry(int(entry), rules[rule]))
        checkAll.append(any(checkEntry))
        if not any(checkEntry):
            getWrongs.append(int(entry))
    return all(checkAll), getWrongs

def get_valids(tickets, rules):
    valids=[]
    for ticket in tickets:
        if check_ticket(ticket,rules)[0]:
            valids.append(ticket)
    return valids


rules, myTicket, tickets=read_input('day16.dat')

rules=process_rules(rules)
# print(rules)
myTicket=process_tickets(myTicket)
print(myTicket)
tickets=process_tickets(tickets)
# print(tickets)

#pt1
allWrongs=[]
for ticket in tickets:
    check, wrongs = check_ticket(ticket, rules)
    allWrongs+=wrongs
print(sum(allWrongs))

#pt2

def check_all_len(possField):
    for k in possField:
        if len(k)>1:
            return False
    return True

allValids=get_valids(tickets,rules)

possField=[]
for field in range(len(myTicket[0])):
    possField.append([])

for field in range(len(myTicket[0])):
    for num, rule in enumerate(rules):
        checkField=[]
        for valid in allValids:
            #checar se valid[field] tá dentro de rules[rule]
            checkField.append(check_entry(valid[field], rules[rule]))
        if all(checkField):
            possField[field].append(rule)

while (not check_all_len(possField)):
    for k in range(len(possField)):
        if len(possField[k])==1:
            for otherK in range(len(possField)):
                if otherK!=k:
                    try:
                        possField[otherK].remove(possField[k][0])
                    except ValueError:
                        pass

mul=1
for k, field in enumerate(possField):
    if 'departure' in field[0]:
        mul*=int(myTicket[0][k])
        print(f'{field[0]}: {myTicket[0][k]}')
print(mul)