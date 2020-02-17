import threading


def func(n):
    while n > 0:
        print("当前线程数:", threading.activeCount())
        n -= 1


threads = []  # 运行的线程列表
for x in range(5):
    t = threading.Thread(target=func, args=(2,))
    threads.append(t)  # 将子线程追加到列表
    t.start()

for t in threads:
    t.join()

print("主线程：", threading.current_thread().name)
