def mount_passport(inp):
    passport={}
    inp=inp.split()
    for item in inp:
        entry=item.split(":")
        passport[entry[0]]=entry[1]
    return passport

def check_cred(passport):
    if all([k in passport for k in ['byr','iyr','eyr','hgt','hcl','ecl','pid']]):
        if int(passport['byr'])<1920 or int(passport['byr'])>2002: return False
        if int(passport['iyr'])<2010 or int(passport['iyr'])>2020: return False
        if int(passport['eyr'])<2020 or int(passport['eyr'])>2030: return False
        hgtUnity=passport['hgt'][-2:]
        if hgtUnity=='cm':
            hgtValue=int(passport['hgt'][0:-2])
            if hgtValue<150 or hgtValue>193: return False
        elif hgtUnity=='in':
            hgtValue=int(passport['hgt'][0:-2])
            if hgtValue<59 or hgtValue>79: return False
        else:
            return False
        if len(passport['hcl']) != 7: return False
        for k in range(len(passport['hcl'])):
            if k==0:
                if passport['hcl'][k] != "#": return False
            else:
                if passport['hcl'][k] not in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']: return False
        if passport['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']: return False
        if len(passport['pid'])!=9: return False
        return True
    return False
    

inp=""
passport=""
valids=0
while(inp!="!"):
    inp=input()
    if(inp=="!"): break
    passport+=" "+inp
    if inp=="":
        mount_passport(passport)
        if (check_cred(mount_passport(passport))): valids+=1
        passport=""

print(valids)
