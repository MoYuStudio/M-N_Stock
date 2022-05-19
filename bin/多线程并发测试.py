
import multiprocessing
import time

def func(msg):
    for i in range(3):
        print(msg)
        time.sleep(1)

if __name__ == "__main__":

    # for i in range(3):
    #     p = multiprocessing.Process(target=func, args=("hello",))
    #     p.start()
    p = multiprocessing.Process(target=func, args=("hello", ))
    p.start()

    p1 = multiprocessing.Process(target=func, args=("hello1", ))
    p1.start()


    p.join()
    p1.join()
    print("Sub-process done.")