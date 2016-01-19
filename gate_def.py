# tautology gate (always true)
def TAUT(a,b):
    return True
    

# nand gate
def NAND(a,b):
    if a == True:
        if b == True:
            return False
        else:
            return True

# converse implication gate
def CIMP(a,b):
    if b == True:
        if a == False:
            return False
    else:
        return True
        

# and gate
def AND(a,b):
    if a == True :
        if b == True :
            return True
    else : 
        return False
        

# or gate
def OR(a,b):
    if a == True:
        return True
    elif b == True:
        return True
    else :
        return False

# nor gate
def NOR(a,b):
    if a == False:
        return True
    elif b == False:
        return True
    else :
        return False

# xor gate
def XOR(a,b) :
    if a != b:
        return True
    else:
        return False
