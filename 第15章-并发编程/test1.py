import queue
import threading
import time


def q_put():
    for i in range(10):
        q.put('1')
    while True:
        q.put('2')

        time.sleep(1)


def q_get():
    while True:
        temp = q.get()
        q.task_done()
        print(temp)
        time.sleep(0.3)


q = queue.Queue()
t1 = threading.Thread(target=q_put)
t2 = threading.Thread(target=q_get)
t1.start()
t2.start()
q.join()
print('queue is empty now')