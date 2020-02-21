from concurrent.futures import ThreadPoolExecutor
import threading


def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().getName() + ' ' + str(i))
        my_sum += i
    return my_sum


with ThreadPoolExecutor(max_workers=4) as pool:
    results = pool.map(action, (50, 100, 150))
    print('----------------')
    for r in results:
        print(r)
