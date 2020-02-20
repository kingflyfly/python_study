import queue
bq = queue.Queue(maxsize=-1)
bq.put('python')
bq.put('python')
print('---------------------------')
print(bq.qsize())
print(bq.empty())

print(bq.get())
print(bq.get())
print(bq.get())