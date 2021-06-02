import time
##可用于装饰 带参数函数 带返回值函数
def decorator(func):
    def inner(*args,**kwargs):
        start=time.perf_counter()
        res=func(*args,**kwargs)
        end=time.perf_counter()
        interval=end-start
        print("用时：{:.2}秒".format(interval))
        return res
    return inner
@decorator
def func(*args,**kwargs):

    return ""
func(1,2,3,key="value")

    
    
