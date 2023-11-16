from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Lock
import time

class Bank:
    def __init__(self):
        self.total = 0
        self.transaction_count = 0
        self.lock = Lock()

    def add(self, amount):
        # with self.lock:
        #     self.total += amount
        #     print(f'Adding {amount}, new total is {self.total}\n')
        time.sleep(1)
        self.total += amount
        print(f'Adding {amount}, new total is {self.total}\n')

    def remove(self, amount):
        # with self.lock:
        #     self.total -= amount
        #     print(f'Removing {amount}, new total is {self.total}\n')
        time.sleep(1)
        self.total -= amount
        print(f'Removing {amount}, new total is {self.total}\n')


bank = Bank()

with ThreadPoolExecutor(max_workers=5) as executor:
    li = [(True, 10), (True, 20), (False, 15), (True, 5), (False, 13)]
    for x, y, in li:
        if x:
            executor.submit(bank.add, y)
        else:
            executor.submit(bank.remove, y)

# t1 = Thread(target=bank.add, args=(10,))
# t2 = Thread(target=bank.add, args=(20,))
# t3 = Thread(target=bank.remove, args=(15,))
# t4 = Thread(target=bank.remove, args=(5,))
# t5 = Thread(target=bank.add, args=(13,))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()