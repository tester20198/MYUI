import threading
from Public.startMultiAppium import MultiAppium


MultiAppium.service()  # 启动多个服务


def multi_thread(*args):
    thread_list = []  # 线程池
    for i in args:
        threading.Thread(target=i)  # 线程
        thread_list.append(i)  # 添加线程进线程池
    for o in thread_list:
        o.setDaemon(True)  # 设置线程为后台线程
        o.start()  # 开始执行线程
    o.join()  # 阻塞主线程，必须所有子线程执行完成才能终止程序


def test_1():











"""
构造方法： 
Thread(group=None, target=None, name=None, args=(), kwargs={}) 

　　group: 线程组，目前还没有实现，库引用中提示必须是None； 
　　target: 要执行的方法； 
　　name: 线程名； 
　　args/kwargs: 要传入方法的参数。

实例方法： 
　　isAlive(): 返回线程是否在运行。正在运行指启动后、终止前。 
　　get/setName(name): 获取/设置线程名。 

　　start():  线程准备就绪，等待CPU调度
　　is/setDaemon(bool): 获取/设置是后台线程（默认前台线程（False））。（在start之前设置）
　　如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程和后台线程均停止
   如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止

　　start(): 启动线程。 
　　join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
"""