
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import time

import decorator

class ConcurrentCore:
    def __init__(self, max_processes=4):
        # self.pool = multiprocessing.Pool(processes=max_processes)
        pass

    def set(self):
        pass

    @decorator.runtime
    def run(self):
        with ProcessPoolExecutor() as pool:
            print(pool.map(self.func))

    def func(self, x):
        for i in range(x):
            print(time.time())
            time.sleep(0.1)

if __name__ == "__main__":

    c = ConcurrentCore()
    c.func(10)
    c.run()