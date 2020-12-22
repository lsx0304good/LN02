import threading
import time


class SubThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "subthread" + self.name + "executes, i = " + str(i)
            print(msg)


if __name__ == "__main__":
    print("---------- main thread starts ----------")
    t1 = SubThread()
    t2 = SubThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("---------- main thread ends ----------")
