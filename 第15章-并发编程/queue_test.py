import queue
bq = queue.Queue()
bq.put('python')
bq.put('python')
bq.put('python')
print('---------------------------')
print(bq.qsize())
print(bq.empty())

print(bq.get())