from threading import Timer
import time

count = 0

def print_time():
    print('当前的时间:%s' % time.ctime())
    global t , count
    count += 1
    if count <= 10:
        t = Timer(1,print_time)
        t.start()
t = Timer(1,print_time)
t.start()