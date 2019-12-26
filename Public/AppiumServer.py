import time
import platform
import subprocess


class AppiumServer:
    """
    管理appium服务
    """

    def start_server(self):
        """
        启动单个appium服务时
        """
        try:
            print('启动Appium服务，默认aport=4723,bport=4724')
            subprocess.Popen('appium')  # mac_OS
            time.sleep(2)  # 等待启动时间
            return True
        except Exception as e:
            print('启动失败，可能端口已被占用，请重试...')
            self.stop_server()
            return False

    def start_server_detail(self, port, device):
        """
        启动多个appium服务时,端口号建议输入4700～4800之间的，且两者不相同
        """

        print('启动Appium多个服务中...')
        cmd = f'appium -a 127.0.0.1 -p {port} -bp {port+1} -U {device}'
        subprocess.Popen(cmd)
        time.sleep(5)

    def stop_server(self):
        """
        区分系统去停止服务
        """

        p = subprocess.Popen('lsof -i:4723', stdout=subprocess.PIPE, shell=True)
        print('端口号为：', p.pid)
        if not p.pid:
            pass
        else:
            try:
                subprocess.Popen(f'kill -9 {p.pid}')
                print('mac OS:停止Appium服务成功！')
            except Exception:
                pass


if __name__ == '__main__':
    AppiumServer().stop_server()
