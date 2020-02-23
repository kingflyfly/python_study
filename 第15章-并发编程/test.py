import threading

def main():
    n = 0
    lock = threading.Lock()
    # lock = threading.RLock()
    with lock:
        for i in range(10):
            n += 1
            with lock:
                print(n)

t1 = threading.Thread(target=main)
t1.start()
