from math import sqrt
class Triangle(object):
    def __init__(self,a,b,c):
        self._a=a
        self._b=b
        self._c=c
    @property
    def a(self):
        return self._a
    @property
    def b(self):
        return self._b
    @property
    def c(self):
        return self._c
    @a.setter
    def a(self,a):
        self._a=a
    @b.setter
    def b(self,b):
        self._b=b
    @c.setter
    def c(self,c):
        self._c=c

    @staticmethod
    def isValid(a,b,c):
        return a+b>c and b+c>a and a+c>b
    def __str__(self):
        return '%d,%d,%d'%(self.a,self.b,self.c)

def main():
    if Triangle.isValid(3,4,5):
        t=Triangle(3,4,5)
        print(t)
    else:
        print('Unable to constract a triangle')
if __name__ == '__main__':
    main()