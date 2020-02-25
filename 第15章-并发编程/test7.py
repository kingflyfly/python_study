import threading
import time
import queue

q = queue.Queue()
"""
    Queue 模块中的 task_done , join
    一个例子解决;
    这个例子将阻塞
    task_done : 用于 get 的后续调用.告诉队列任务处理完成.当然你也可以不调用get
    join: 阻塞操作,直到队列所有的任务都处理. 
          大白话是你往里 put 几次,就要调用task_done几次,自己可以试下
"""


def worker(q1):
    time.sleep(0.5)
    item = q.get()  # 获取
    print('{} get {} , {} left'.format(threading.currentThread().ident, item, q1.qsize()))
    q1.task_done()  # 处理完成


for i in range(5):  # 创建5个线程去获取
    t = threading.Thread(target=worker, args=(q,))
    t.start()
for i in range(10):
    q.put([chr(i), i])  # 入队10个
print('main thread running')
q.join()  # 阻塞,直到调用10次task_done
