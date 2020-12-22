from multiprocessing import Queue

if __name__ == '__main__':
    q = Queue(3)
    q.put("message 1")
    q.put("message 2")
    print(q.full())
    q.put("message 3")
    print(q.full())

    try:
        q.put("message 4", True, 2)
    except:
        print("the queue is full, it curretly has %s messages." % q.qsize())

    try:
        q.put_nowait("message 4")
    except:
        print("the queue is full, it curretly has %s messages." % q.qsize())

    if not q.empty():
        print("get message from the queue")
        for i in range(q.qsize()):
            print(q.get_nowait())

    if not q.full():
        q.put_nowait("message 4")