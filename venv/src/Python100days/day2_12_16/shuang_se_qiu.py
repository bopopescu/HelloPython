from random import randrange, randint, sample
def radSelect():
    redBalls=[x for x in range(1,34)]
    selectedBalls=[]
    selectedBalls=sample(redBalls,6)
    selectedBalls.sort()
    selectedBalls.append(randint(1,15))
    return selectedBalls

def caclPrize(yourNum,winningNum):
    if yourNum==winningNum:
        return 8000000-2
    elif yourNum[-1]==winningNum[-1]:
        return 5-2
    return 0-2

if __name__=='__main__':
    sum=0
    for _ in range(500):
        sum+=caclPrize(radSelect(),radSelect())
    print(sum)