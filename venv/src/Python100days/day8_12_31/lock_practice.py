from time import time, sleep
from threading import Thread, Lock

class Account(object):
    def __init__(self):
        self._balance=0
        self._lock=Lock()

    def deposite(self,money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()


    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self,Account,money):
        super().__init__()
        self._Account=Account
        self._money=money

    def run(self) -> None:
        self._Account.deposite(self._money)


def main():
    myAccount=Account()
    threads=[]
    for _ in range(200):
        t=AddMoneyThread(myAccount,1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print('I have $ %d'%myAccount.balance)

if __name__ == '__main__':
    main()
