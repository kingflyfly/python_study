import queue
import time
print(time.time())
bq = queue.Queue(maxsize=-1)
bq.put('python')
bq.put('python')
print('---------------------------')
print(bq.qsize())
print(bq.empty())

print(bq.get())
print(bq.get())
try:
# print(bq.get_nowait())
    bq.get_nowait()
except queue.Empty as  e:
    print(e)