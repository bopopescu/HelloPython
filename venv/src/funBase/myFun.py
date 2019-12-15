def myAbs(x):
    if x<0:
        return -x
    else:
        return x
def nop():
    pass

def power(x,n=2):
    s=1
    while n>0:
        s=s*x
        n-=1

    return s
def enrole(name,gendel,age=6,city='Heze'):
    print('name:',name)
    print('gendel:',gendel)
    print('age:',age)
    print('city:',city)

def addEnd(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

def person(name,age,*,city,job):
    print('name=',name)
    print('age=',age)
    print(city,job)

def f1(a,b,c=0,*,job,**kw):
    print(a,b,c,job,kw)

def product(*x):
    pro=1
    for num in x:
        pro=num*pro
    return pro
extra={'job':'Enginner','city':'Beijing'}
nums=[1,2,3]
print(myAbs(-3))
print(power(5))
enrole('Xiaoming','F',city='New York')
print(addEnd(['Heihei']))
print(calc(1,2,3))
print(calc(nums[0],nums[1]))
print(calc(*nums))
print()
print(person('Amy',5,city='Beijing',job='Worker'))

args=(1,2,3)
myKw={'job':'Eng','gender':'F'}
print(f1(*args,**myKw))
print(product(1,2,3))