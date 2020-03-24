import queue
import threading
import time


def main(bq1):
    b = True
    while b:
        try:
            a = bq1.get_nowait()
        except queue.Empty:
            b = False
        else:
            print(threading.current_thread().name + ' ' + str(a))


if __name__ == '__main__':
    start_time = time.time()
    bq = queue.Queue(maxsize=-1)
    for i in range(10000):
        bq.put(i)
    for j in range(30):
        threading.Thread(target=main, args=(bq,)).start()
    end_time = time.time()
    print('time', end_time - start_time)
