from threading import Thread
import time

def plus():
    print("----- subthread1 starts -----")
    global g_num
    g_num += 50
    print('g_num is %d' % g_num)
    print("----- subthread1 ends -----")

def minus():
    global g_num
    time.sleep(1)
    print("----- subthread2 starts -----")
    g_num -= 50
    print('g_num is %d' % g_num)
    print("----- subthread2 ends -----")

g_num = 100
if __name__ == "__main__":
    print("----- main thread starts -----")
    print('g_num is %d' % g_num)
    t1 = Thread(target=plus)
    t2 = Thread(target=minus)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("----- main thread ends -----")
