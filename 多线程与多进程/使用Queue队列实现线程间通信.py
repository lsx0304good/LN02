import random
import threading
import time
from queue import Queue


class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            print("Producer %s is adding product %d into the queue ..." % (self.getName(), i))
            self.data.put(i)
            time.sleep(random.random())
        print("Producer %s done!" % self.getName())


class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print("Consumer %s is grabbing product %d out of the queue ..." % (self.getName(), val))
            time.sleep(random.random())
        print("Consumer %s done!" % self.getName())


if __name__ == '__main__':
    print("----- main thread starts -----")
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer', queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print("----- main thread ends -----")
