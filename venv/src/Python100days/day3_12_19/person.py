class Person(object):

    def __init__(self,name,age):
        self._name=name
        self._age=age

    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age=age
    @name.setter
    def name(self,name):
        self._name=name

    def play(self):
        print('%s is playing'%self.name)

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self._grade=grade
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self,grade):
        self._grade=grade
    def study(self,course):
        print('%s is study %s'%(self._name,course))


def main():
    p=Person('Kiki',18)
    p.play()
    stu=Student('Tom',18,60)
    stu.study('English')


if __name__ == '__main__':
    main()