import threading
import time

class Account(object):
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self.balance = balance

def draw(account,draw_amount):
    if account.balance >= draw_amount:
        print(threading.current_thread().name+"取钱成功! 吐出钞票:"+str(draw_amount))
        time.sleep(0.001)
        account.balance -= draw_amount
        print('余额'+str(account.balance))
    else:
        print(threading.current_thread().name+"取钱失败,余额不足!")
acct = Account('123456',1000)
threading.Thread(name='甲',target=draw,args=(acct,800)).start()
threading.Thread(name='乙',target=draw,args=(acct,800)).start()