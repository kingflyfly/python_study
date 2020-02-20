import threading
import queue
import time


def product(bq1):
    str_tuple = ('Python', 'Kotlin', 'Swift')
    for i in range(9999):
        print(threading.Thread().name + "生产者准备生产元组元素")
        time.sleep(0.2)
        bq1.put(str_tuple[i % 3])
        print(threading.Thread().name + "生产者生产元组元素完成")


def consume(bq1):
    print(threading.Thread().name + "消费者准备消费元组元素")
    time.sleep(0.2)
    t = bq1.get()
    print(threading.Thread().name + "消费者消费[%s]元素" % t)


bq = queue.Queue(1)
threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()
threading.Thread(target=product, args=(bq,)).start()

threading.Thread(target=consume, args=(bq,)).start()
