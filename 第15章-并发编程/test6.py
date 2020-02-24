import threading
import time
import queue


class Mythread(threading.Thread):
    def __init__(self,que):
        threading.Thread.__init__(self)
        self.queue = que
    def run(self):
        while 1:
            time.sleep(1)
            if self.queue.empty():
                break
            item = self.queue.get()
            print(item,'!')
            self.queue.task_done()
        return
que = queue.Queue()
tasks = [Mythread(que) for x in range(1)]
print(tasks)
for x in range(10):
    que.put(x)
for x in tasks:
    t = Mythread(que)
    t.start()
que.join()
print('---success---')
