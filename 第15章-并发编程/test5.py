from queue import Queue
import time
import threading
#生产消费模型
q = Queue(maxsize=10)

def product(name):
    count = 1
    while True:
        q.put('步枪{}'.format(count))
        print('{}生产步枪{}支'.format(name,count))
        count+=1
        time.sleep(0.3)

def cousume(name):
    while True:
        print('{}装备了{}'.format(name,q.get()))
        time.sleep(0.3)
        # q.task_done()


#部队线程
p = threading.Thread(target=product,args=('张三',))
k = threading.Thread(target=cousume,args=('李四',))
w = threading.Thread(target=cousume,args=('王五',))

p.start()
k.start()
w.start()