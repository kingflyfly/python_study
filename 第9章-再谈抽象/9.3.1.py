def check_index(key):
    """
    指定的键是否是可接受的索引？
    键必须是非负整数，才是可接受的。如果不是整数，
    将引发TypeError异常；如果是负数，将引发Index
    Error异常（因为这个序列的长度是无穷的）
    """
    if not isinstance(key,int):raise TypeError
    if key < 0: raise IndexError
class  ArithmeticSequence:
    def __init__(self,start=0,step=1):
        """
        初始化这个算术序列
        start -序列中的第一个值
        step -两个相邻值的差
        changed -一个字典，包含用户修改后的值
        """
#        print(self)
        self.start = start
        self.step = step
        self.change = {}
    def __getitem__(self,key):
        """
        从算术序列中获取一个元素
        """
        check_index(key)
        try:return self.change[key]                 # 修改过？
        except KeyError:                            #如果没有修改过，就计算元素的值
            return self.start + key * self.step

    def __setitem__(self, key, value):
        """
        修改算术序列中的元素
        """
        check_index(key)
        self.changed[key] = value

s = ArithmeticSequence(1, 3)
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
s[3] = 2


