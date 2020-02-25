import threading
import queue
from time import sleep

que = queue.Queue()


class Testthread(threading.Thread):
    def __init__(self, que1):
        threading.Thread.__init__(self)
        self.queue = que1

    def run(self):
        while True:
            sleep(0.1)
            item = self.queue.get()
            print(item)
            self.queue.task_done()


tasks = [Testthread(que) for x in range(2)]
print(tasks)

for x in tasks:
    t = Testthread(que)
    t.setDaemon(True)
    t.start()

for x in range(10):
    que.put(x)
que.join()

print('all done')
