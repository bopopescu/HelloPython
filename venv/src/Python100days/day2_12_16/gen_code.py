import random

def genRadCode():
    codelen=4
    str='shfdakjHIHk661321651615'
    lastPos=len(str)-1
    code=''
    for ch in range(codelen):
        code+=str[random.randint(0,lastPos)]
    return code

print(genRadCode())