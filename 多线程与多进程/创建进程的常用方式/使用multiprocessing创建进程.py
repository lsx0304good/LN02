from multiprocessing import Process


def test(interval):
    print("I am sub-process")


def main():
    print("main process starts")
    p = Process(target=test(1,))
    p.start()
    print("main process ends")


if __name__ == "__main__":
    main()
