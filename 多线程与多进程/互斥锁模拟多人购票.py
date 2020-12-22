from threading import Thread, Lock
import time

n = 100


def task():
    global n
    mutex.acquire()
    temp = n
    time.sleep(0.1)
    n = temp - 1
    print('payment was successful, %d tickets left' % n)
    mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    t_l = []
    for i in range(10):
        t = Thread(target=task)  # 实例化线程
        t_l.append(t)
        t.start()
    for t in t_l:
        t.join()
