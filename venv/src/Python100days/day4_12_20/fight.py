from abc import ABCMeta,abstractmethod
from random import randint,randrange

class Fighter(object,metaclass=ABCMeta):
    __slots__ = ('_name','_hp')

    def __init__(self,name,hp):
        self._name=name
        self._hp=hp

    @property
    def name(self):
        return self._name
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,hp):
        self._hp=hp if hp>0 else 0

    def isAlive(self):
        return self._hp>0
    @abstractmethod
    def attack(self,other):
        pass

class Ultraman(Fighter):
    __slots__ = ('_name','_hp','_mp')
    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp=mp

    def attack(self,other):
        other.hp-=randint(15,25)

    def ultimateSkill(self,other):
        if self._mp>=50:
            self._mp-=50
            other.hp-=60
            return True
        else:
            self.attack(other)
            return False

    def magicAttack(self,others):
        if self._mp>=20:
            self._mp-=20
            for m in others:
                if m.isAlive:
                    m._hp-=randint(10,20)
            return True
        else:
            return False

    def resume(self):
        dmp=randint(1,30)
        self._mp+=dmp
        return dmp

    def __str__(self):
        return '%s\nHP:%d\nMP:%d\n'%(self.name,self.hp,self._mp)

class Monster(Fighter):
    __slots__ = ('_name','_hp')
    def __init__(self,name,hp):
        super().__init__(name,hp)
    def attack(self,other):
        other.hp-=randint(10,20)
    def __str__(self):
        return '%s\nHP:%d'%(self.name,self.hp)

def isAnyAlive(monsters):
    for m in monsters:
        if m.hp>0:
            return True
    return False

def selectOneAlive(monsters):
    mLen=len(monsters)
    while True:
        index = randrange(mLen)
        monster = monsters[index]
        if monster.isAlive:
            return monster
def board(u,m):
    print(u)
    for mo in m:
        print(mo)

def main():
    u=Ultraman('Blayt',1000,100)
    ms=[Monster('Cat',100),Monster('Dog',100),Monster('Cow',100)]
    fRound=1
    while u.isAlive() and isAnyAlive(ms):
        print('\nRound %02d'%fRound)
        m=selectOneAlive(ms)
        skill=randint(1,10)
        if skill<=5:
            print('%s beat %s'%(u.name,m.name))
            u.attack(m)
            u.resume()
        elif skill<=9:
            if u.magicAttack(ms):
                print('%s AOE!!!!!!' % u.name)
            else:
                print('MP not enough!')

        else:
            if u.ultimateSkill(m):
                print('%s is using ultimate skill'%u.name)
            else:
                print('MP not enough!\nNormal attack instead')
                u.resume()

        if m.isAlive():
            m.attack(u)
            print('%s attacks U'%m.name)
        board(u,ms)
        fRound+=1
    print('Finish')
    if u.isAlive():
        print('The winner is U')
    else:
        print('Winners are monsters')


if __name__ == '__main__':
    main()

