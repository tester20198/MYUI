import time
import os, random
from Public.AndroidMessage import Android


class MultiAppium:
    """
    启动多个appium服务
    """

    aport = random.randint(4700,4750)  # 随机Server Port，Appium端
    bport = random.randint(4751,4800)  # 随机Bootstrap Port，安卓端

    def service(self):
        """start multi appium server"""

        try:
            print('启动Appium中... ...')
            for i in self.dev():
                if len(self.dev()) > 1:
                    print('当前设备数大于2')
                    # 启动appium命令行(-p:port /-U:udid /-bp:bootstrap port)  注意：start /b是启动服务而不启动窗体
                    cmd = f'start /b appium -a 127.0.0.1 -p {self.aport} -bp {self.bport} -U {i}'
                    os.system(cmd)  # 执行命令行
                    time.sleep(10)  # 等待服务响应,服务启动需要时间
                else:
                    print('多线程，设备数须大于1')
        except:
            print('启动Appium失败... ...')
            os._exit(0)  # 停止执行命令

    def dev(self) -> list:
        # 设备组
        return Android.get_android_name()
