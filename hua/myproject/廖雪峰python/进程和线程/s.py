import multiprocessing
import time


def write(q):
    for value in ['a', 'b', 'c']:
        print("已经输入:", value)
        q.put(value)
        time.sleep(1)


def read(q):
    while True:
        if not q.empty():
            print('获取的数据是：', q.get())
            time.sleep(1)
        else:
            break


if __name__ == '__main__':
    q = multiprocessing.Queue()
    pw = multiprocessing.Process(target=write, args=(q,))
    pr = multiprocessing.Process(target=read, args=(q,))
    pw.start()
    pw.join()

    pr.start()
    pr.join()
    print('接收完毕')