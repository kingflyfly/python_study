import threading


def action(max1):
    for j in range(max1):
        print(threading.current_thread().name + " " + str(j))


threading.Thread(target=action, args=(100,), name='新线程').start()
for i in range(100):
    if i == 20:
        jt = threading.Thread(target=action, args=(100,), name="被join的线程")
        jt.start()
        jt.join(timeout=None)
    print(threading.current_thread().name + " " + str(i))
