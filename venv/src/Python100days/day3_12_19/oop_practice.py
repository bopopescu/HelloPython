class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def study(self,courseName):
        print('%s is studying %s'%(self.name,courseName))
    def surfInt(self):
        if self.age<18:
            print('Watching math online classes')
        else:
            print('Watching pornhub')

def main():
    stu1=Student('kiki',18)
    stu1.study('Java')
    stu1.surfInt()


if __name__ == '__main__':
    main()