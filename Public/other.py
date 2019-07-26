import time
import os
import random
import string


def format_time(format='%Y-%m-%d'):
    """
    时间格式化输出
    :return:年-月-日 时：分：秒
    """

    dt = time.strftime(format, time.localtime(time.time()))
    return dt


def current_path():
    """
    :return:获取当前文件所在文件夹位置
    """

    path = os.getcwd()
    return path


def upper_path():
    """
    :return:获取上一级文件夹位置
    """

    path = os.path.dirname(os.getcwd())
    return path + '/'


def self_path(way):
    """
    :way:调用者的__file__
    :return:返回自身所在的位置
    """

    path = os.path.abspath(way)
    return path


def append_path(name):
    """
    更改父级文件夹下的目录(mac os)
    :param name:文件夹名称
    :return:
    """

    if name.endswith('/'):
        pass
    else:
        name = name + '/'
    path = os.path.join(current_path(), name)
    return path


def other_dic(file):
    """
    转到同父级的文件夹
    :param file:
    :return:
    """

    if file.endswith('/'):
        pass
    else:
        file = file + '/'
    path = os.path.join(upper_path(), file)
    return path


# -------------------------------随机生成数据部分------------------------------- #
def create_mobile():
    """
    随机生成电话号码
    :return:
    """

    num = '0123456789'
    # code = ['+86137', '+86159', '+86188', '+86132']  # 中国
    code = ['4120','4123','4124']  # 委内瑞拉
    mobile = random.choice(code) + ''.join(random.choice(num) for i in range(6)) # 委内瑞拉
    return mobile

def create_email():
    """
    随机生成邮箱地址
    :return:
    """

    num = '0123456789'
    server = ['@qq.com', '@163.com']  # 邮箱域名
    email = ''.join(random.choice(num) for i in range(8)) + random.choice(server)
    return email


def create_address(size=6, chars=string.digits + string.ascii_letters):
    """
    随机生成字符串（字母+数字）
    :param size: 随机生产字符串的长度
    :param chars: 字符串范围（字母+数字)
    :return:
    """

    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == '__main__':
    print(create_email())