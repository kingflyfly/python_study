import threading
class FKThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.i = 0
    def run(self):
        while self.i < 100:
            print(threading.current_thread().getName()+ " "+ str(i))
            self.i += 1

for i in range(100):
    print(threading.current_thread().getName()+ " "+ str(i))
    if i == 20:
        ft1 = FKThread()
        ft1.start()
        ft2 = FKThread()
        ft2.start()
print('主线程执行完成')

