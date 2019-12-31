from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print('Process %d start to work, downloading %s'%(getpid(),filename))
    time_spent=randint(5,10)
    sleep(time_spent)
    print('It tokes %d s to download'%time_spent)

def main():
    start_time=time()
    p1=Process(target=download_task,args=('My heart will go on.mp3',))
    p1.start()
    p2=Process(target=download_task,args=('The wolf of wall street',))
    p2.start()
    p1.join()
    p2.join()
    end_time = time()
    print('总共耗费了%.2f秒.' % (end_time - start_time))


if __name__ == '__main__':
    main()
