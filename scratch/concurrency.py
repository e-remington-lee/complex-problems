'''
helpful reminder with examples for concurrency, 
    non-blocking processes (map/apply async)
    blocking processes (map/apply)
    multiple argument processes (starmap/ starmap_asnc)
    wait for async calls (map/apply _async returns a ApplyResult object, call .get() on this and it will block and wait for the return object)
    chain async calls
    https://stackoverflow.com/questions/8533318/multiprocessing-pool-when-to-use-apply-apply-async-or-map
    https://stackoverflow.com/questions/38271547/when-should-we-call-multiprocessing-pool-join
    https://e2eml.school/multiprocessing.html
'''
import os
import time
import multiprocessing
# from concurrent.futures import ProcessPoolExecutor
from multiprocessing import RLock
import threading
from typing import *

class Bank(object):
    def __init__(self, balance=0):
        self.balance=balance
        self.mp_results=[]

    def check_balance(self, read_lock:RLock) -> int:
        print(self.balance)
        return self.balance

    def deposit(self, amount) ->int:
        self.balance+=amount
        print(self.balance)
        return self.balance

    def withdraw(self, amount)->int:
        self.balance-=amount
        print(self.balance)
        return self.balance

    def square(self, i):
        x=i*i
        print(x)
        return x

    def log(self, result):
        print(os.getpid())
        self.mp_results.append(result)

    @staticmethod
    def infinite_glitch():
        while True:
            print("i")

class Bob:
    def test(self):
        li = []
        for i in range(2):
            time.sleep(0.5)
            print('b')
            li.append('b')
        return li


def test(x):
    print("start process")
    time.sleep(x)
    print("end process")

# How can you pass a lock class between processes if python cannot pickle classes? python has special features for this, or use a pool manager
# https://stackoverflow.com/questions/25557686/python-sharing-a-lock-between-processes#:~:text=With%20a%20Pool%20%2C%20when%20you,the%20Lock%20can%20be%20passed.
def ihatelife():
    pool = multiprocessing.Pool()
    a = pool.apply_async(test, (2,))
    b = pool.apply_async(test, (2,))
    print("main script")
    print("end main script")
    a.wait()
    b.wait()

def mytest():
    pool = multiprocessing.Pool()
    start=time.time()
    li = [Bob() for _ in range(3)]
    futures = []
    with multiprocessing.Pool(processes=3) as pool:
        for b in li:
            f = pool.apply_async(b.test)
            futures.append(f)
        
        print(time.time()-start)
        print('not blocked')
        while not futures[0].ready():
            print("idfk")
            time.sleep(1)
        # print([f.get(10) for f in futures])


if __name__ == "__main__":
    # ihatelife()
    mytest()
    pass
    bank = Bank(200)
    read_lock = RLock()
    # write_lock = Lock()


    ## multiprocessing blocking/non-blocking methods
    ## the non-blocking is certainly faster, it is not easy to see here because the tasks are so quick, but if they were long it would be obvious
    # with multiprocessing.Pool(processes=10) as p:
    #     li=range(50)
    #     start=time.time()
    #     result=p.map_async(bank.square, li)
    #     print('this is shown while/before functions are ran')
    #     p.close()
    #     '''
    #     without join(), the main method will not wait for the processes to be finished, so the processes in progress will be discarded
    #     by adding the time.sleep, you can see that sometimes half the processes are run before it is cut off, sometimes they all run.
    #     it does not wait for all of them to complete before cutting off the main thread, so we do not always see them all
    #     '''
    #     # time.sleep(0.055)
    #     p.join()
    #     print(time.time()-start)

    # with multiprocessing.Pool(processes=10) as p:
    #     li=range(50)
    #     start=time.time()
    #     r=[]
    #     r.append(p.map(bank.square, li))
    #     print('functions are ran before this is shown')
    #     p.close()
    #     p.join()
    #     # print(r)
    #     print(time.time()-start)




