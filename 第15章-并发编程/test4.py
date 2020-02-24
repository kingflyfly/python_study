import queue

q = queue.Queue(maxsize=2)
try:
    q.put_nowait('1')
    q.put_nowait('2')
    # q.put_nowait('3')
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()
except queue.Full as e:
    print('full')
except queue.Empty as e:
    print('empty')