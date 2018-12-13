import os, subprocess
from Public.getConfig import Environment
import Public.other as other


def write_log():
    """
    写入app日志
    :return:
    """

    en = Environment()
    app = en.get_env('app', 'app')  # 获取待测试app名字
    tt = other.format_time()  # 时间格式化
    file = os.path.join(os.path.dirname(os.getcwd()), f'logs/{tt}{app}.log')
    cmd = f'adb shell logcat -v time | grep {app} > {file}'  # 查看app日志命令
    print('执行的终端命令是:', cmd)
    process = subprocess.Popen(cmd, shell=True)
    return process


def stop_log():
    """
    停止写入app日志
    :return:
    """

    write_log().kill()