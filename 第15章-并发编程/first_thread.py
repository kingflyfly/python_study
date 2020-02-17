import threading


def action(max):
    for j in range(max):
        print(threading.current_thread().getName() + "----" + str(j))


for i in range(100):
    print(threading.current_thread().getName() + "----" + str(i))
    if i == 20:
        t1 = threading.Thread(target=action, args=(100,))
        t1.start()
        t2 = threading.Thread(target=action, args=(100,))
        t2.start()
print('主线程执行完成!')
