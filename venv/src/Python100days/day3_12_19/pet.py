from abc import ABCMeta,abstractmethod

class Pet(object,metaclass=ABCMeta):
    def __init__(self,nickname):
        self._nickname=nickname
    @abstractmethod
    def makeVoice(self):
        pass
class Dog(Pet):
    def makeVoice(self):
        print('%s Wang!!!!!'%self._nickname)
class Cat(Pet):
    def makeVoice(self):
        print('%s Miao!!!!'%self._nickname)
def main():
    pets=[Dog('kiki'),Cat('miaomiao'),Dog('Wangcai')]
    for p in pets:
        p.makeVoice()
if __name__ == '__main__':
    main()