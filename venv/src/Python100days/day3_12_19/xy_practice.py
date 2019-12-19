from math import sqrt

class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def moveTo(self,point):
        self.x=point.x
        self.y=point.y
    def moveBy(self,dx,dy):
        self.x+=dx
        self.y+=dy
    def distanceTo(self,other):
        dx=self.x-other.x
        dy=self.y-other.y
        return sqrt(dx**2+dy**2)
    def __str__(self):
        return '(%s,%s)'%(self.x,self.y)
def main():
    p1=Point(12,54)
    p1.moveTo(Point(5,9))
    print(p1)
    p1.moveBy(2,5)
    print(p1)
    print(p1.distanceTo(Point(0,0)))

if __name__ == '__main__':
    main()