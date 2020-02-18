import queue
bq = queue.Queue(maxsize=10)
bq.put('python')
bq.put('python')
bq.put('python')
print('---------------------------')
print(bq.qsize())
print(bq.empty())
print(bq.get())