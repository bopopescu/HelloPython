import random

class Card(object):
    def __init__(self,suite,face):
        self._suite=suite
        self._face=face

    @property
    def suite(self):
        return self._suite

    @property
    def face(self):
        return self._face

    def __str__(self):
        if self._face==1:
            faceStr='A'
        elif self._face==11:
            faceStr='J'
        elif self._face==12:
            faceStr='Q'
        elif self._face==13:
            faceStr='K'
        else:
            faceStr=str(self._face)
        return '%s%s'%(self._suite,self._face)
    def __repr__(self):
        return self.__str__()

class Poker(object):
    def __init__(self):
        self._cards=[Card(suite,face)
                     for suite in '♠♥♣♦'
                     for face in range(1,14)]
        self._current=0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        self._current=0
        random.shuffle(self._cards)

    @property
    def next(self):
        card=self._cards[self._current]
        self._current+=1
        return card

    @property
    def hasNext(self):
        return self._current<len(self._cards)

class Player(object):
    def __init__(self,name):
        self._name=name
        self._cardsOnHand=[]

    @property
    def name(self):
        return self._name
    @property
    def cardsOnHand(self):
        return self._cardsOnHand

    def getCard(self,card):
        self._cardsOnHand.append(card)

    def arrange(self,cardKey):
        self._cardsOnHand.sort(key=cardKey)

def getCardKey(card):
    return (card.suite,card.face)

def main():
    p=Poker()
    p.shuffle()
    players=[Player('Kiki'),Player('Bob'),Player('Amy'),Player('Alice')]
    for _ in range(13):
        for player in players:
            player.getCard(p.next)
    for player in players:
        print(player.name)
        player.arrange(getCardKey)
        print(player.cardsOnHand)

if __name__ == '__main__':
    main()