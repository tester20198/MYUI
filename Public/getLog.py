import os, subprocess
from Public.getConfig import Environment
import Public.other as other
import logging
import time

def write_log():
    """
    写入app日志
    :return:
    """

    en = Environment()
    app = en.get_env('app', 'app')  # 获取待测试app名字
    tt = other.format_time()  # 时间格式化
    if 'testcase' in os.getcwd():
        file = os.path.join(other.upper_path(), f'logs/{tt}{app}.log')
    else:
        file = os.path.join(os.getcwd(), f'logs/{tt}{app}.log')
    cmd = f'adb shell logcat -v time | grep {app} > {file}'  # 查看app日志命令
    print('运行的日志位置是:', cmd)
    process = subprocess.Popen(cmd, shell=True)
    return process


def stop_log():
    """
    停止写入app日志
    :return:
    """

    write_log().kill()

cur_path = os.path.dirname(os.path.realpath(__file__))  #当前文件路径
def Screenshot(driver):
    '''截图函数'''

    casepath = os.path.join(os.path.dirname(cur_path), './img')  # casepath是存放截图的路径
    if not os.path.exists(casepath):  # 判断路径是否存在，如果不存在，创建文件夹
        os.mkdir(casepath)
    current_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    img_path = casepath + '/' + current_time + '.png'
    # print(img_path)
    driver.get_screenshot_as_file(img_path)
    # driver.save_screenshot(img_path)


def InsertLog(name='root'):
    '''获取错误日志函数'''

    log_path = os.path.join(os.path.dirname(cur_path), 'logs')  # log_path是存放日志的路径
    if not os.path.exists(log_path):  # 如果不存在这个log文件夹，就自动创建一个
        os.mkdir(log_path)
    # 日志输出格式
    setmatter = '%(asctime)s => %(filename)s:%(funcName)s - %(levelname)s - %(message)s'
    datematter = '%Y-%m-%d %H:%M:%S'
    # 文件的命名
    logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d_%H'))
    # 创建logger日志器，如果name为空则返回root
    logger = logging.getLogger(name)
    # 设置日志等级：debug->info->warning->error
    logger.setLevel(logging.DEBUG)

    # 判断logger.handlers列表为空则添加，否则直接使用原handler处理器写日志
    if not logger.handlers:
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(logname, encoding='utf-8')  # 若已有日志，则追加写入
        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()  # 将日志发送到Steam

        # 设置handlers处理器的日志输出格式
        formatter = logging.Formatter(fmt=setmatter, datefmt=datematter)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger日志器添加上创建好的处理器handlers
        logger.addHandler(fh)
        logger.addHandler(ch)

    #     logger.removeHandler(fh)
    #     logger.removeHandler(ch)
    #      避免日志输出重复
    return logger

if __name__ == '__main__':
    InsertLog()