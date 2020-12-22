# -*- coding:utf-8 -*-
import threading, time


def process():
    for i in range(3):
        time.sleep(1)
        print('thread name is {s}'.format(s=threading.current_thread().name))


if __name__ == "__main__":
    print("main thread starts ...")
    threads = [threading.Thread(target=process) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("main thread ends ...")