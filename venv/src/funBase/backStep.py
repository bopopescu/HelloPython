def fa(x):
    if x!=1:
        return fa(x-1)*x
    else:
        return 1

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fa(5))
print(fact(3))