import time
import threading
import pymysql
from queue import Queue

class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, idQueue):
        # 继承父类的方法
        super(ThreadCrawl, self).__init__()
        self.threadName = threadName          # 线程名字
    def run(self):
        print('启动' + self.threadName)
        while not self.idQueue.empty():
            try:
                id = self.idQueue.get(False)  # False 如果队列为空，抛出异常
                time.sleep(1)
                print("~"*300)
                self.get_con(id)

            except Exception as e:
                print('队列为空。。。。。', e)
                pass
            print('#'*300)

    def get_con(self):  #自己封装的请求自定义
        pass
def get_id(m, n):
    conn = pymysql.connect(database='postgres', user='postgres', password='123456', host='127.0.0.1', port='5432')
    cur = conn.cursor()
    sql1 = 'SELECT doc_id from id LIMIT {} offset {};'.format(m, n)
    cur.execute(sql1)
    data = cur.fetchall()
    conn.commit()
    return data
def main():
    n = 60
    while True:
        m = 20
        # m是固定值，一次去20条， n是第几条开始
        print('开始采集n的值为', n)
        if n == 200000:
            break

        # id的队列
        idQueue = Queue(20)
        if idQueue.empty():
            data = get_id(m, n)
            for i in data:
                idQueue.put(i[0])

        #　采集线程的数量
        crawlList = []
        for id in range(1, 2):
            name = '采集线程{}'.format(id)
            print(id)
            crawlList.append(name)

        # 存储采集线程的列表集合
        threadcrawl = []
        for threadName in crawlList:
            thread = ThreadCrawl(threadName, idQueue)
            thread.start()
            threadcrawl.append(thread)

        for thread in threadcrawl:
            thread.join()
        n = n + m
    print("主线程退出..............")
if __name__ == '__main__':
    main()