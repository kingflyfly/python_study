import threading

balance = 0
def change_it_without_lock(n):
    global balance
    # 不加锁的话 最后的值不是0
    # 线程共享数据危险在于 多个线程同时改同一个变量
    # 如果每个线程按顺序执行，那么值会是0， 但是线程时系统调度，又不确定性，交替进行
    # 没锁的话，同时修改变量
    # 所以加锁是为了同时只有一个线程再修改，别的线程表一定不能改
    if lock.acquire():
        try:
            for i in range(100000):
                balance = balance + n
                balance = balance - n
        finally:
            lock.release()
threads = [
    threading.Thread(target=change_it_without_lock, args=(8,) ),
    threading.Thread(target=change_it_without_lock, args=(10,) )
]

lock = threading.Lock()
[t.start() for t in threads]
[t.join() for t in threads]
print(balance)
