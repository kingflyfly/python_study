import sched, time
import threading

s = sched.scheduler()

def print_time(name='default'):
    print('%s 的时间:%s' %(name,time.ctime()))
print('主线程：',time.ctime())
s.enter(10,1,print_time)
s.enter(5,2,print_time,argument=('weizhicanshu',))
s.enter(5,1,print_time,kwargs={'name':'guanjiancicansu'})
s.run()
print('zhuxiancheng:',time.ctime())