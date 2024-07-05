def AND(a,b):
    if a==1 and b==1:
        return True
    else:
        return False


def OR(a, b):
    if a == 1 or b == 1:
        return True
    else:
        return False


def NOT(a, b):
    if a == 0:
        return True
    else:
        return False


def XOR(a, b):
    if a == 1 and b==1 or a==0 and b==0:
        return False
    else:
        return True



print("if A = true & B = true _then   A&B = true",AND(1,1))
print("if A = true & B = false _then  A&B = False",AND(1,0))
print("if A = true & B = false _then  A&B = False",AND(0,1))
print("if A = true & B = false _then  A&B = False",AND(0,0))
print()

print("if A = true & B = true _then  A|B = true",OR(1,1))
print("if A = true & B = false _then A|B = False",OR(1,0))
print("if A = true & B = false _then A|B = False",OR(0,1))
print("if A = true & B = false _then A|B = False",OR(0,0))
print()

print("if A = true & B = true _then   A^B = true",XOR(1,1))
print("if A = true & B = false _then  A^B = False",XOR(1,0))
print("if A = true & B = false _then  A^B = False",XOR(0,1))
print("if A = true & B = false _then  A^B = False",XOR(0,0))
print()

print("if A = true & B = true _then   A!B = true",NOT(1,1))
print("if A = true & B = false _then  A!B = False",NOT(1,0))
print("if A = true & B = false _then  A!B = False",NOT(0,1))
print("if A = true & B = false _then  A!B = False",NOT(0,0))
print()