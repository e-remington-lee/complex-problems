# importing libraries
import random
import time
from threading import Thread

# target function which takes a time at random(from 0 to 2 seconds) to simulate some "work"
def worker(instance):
    time_taken = random.uniform(0, 2)
    time.sleep(time_taken)
    print('thread %s : completed in %s sec' % (instance, time_taken))


if __name__ == '__main__':
    for i in range(0, 10):
        # don't confuse with the variable "t" it is not bound to any thread! it is just a name
        t = Thread(target=worker, args=(i,))
        # starting the thread which will continue working in background after this.
        t.start()
        print('starting')
    print('not blocked')