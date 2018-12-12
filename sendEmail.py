import zmail
from Public import other
from run_report import RunReport
from Public.getConfig import Environment
import os


dd = other.format_time('%Y-%m-%d')


def get_file():
    """
    获取报告文件绝对地址
    若不存在则产生测试报告
    :return:
    """

    filepath = other.append_path('reports')  # 获取报告文件夹绝对地址
    print(f'输出的测试报告路径为：{filepath}')
    f = os.listdir(filepath)  # 列出该文件夹的所有文件
    dex = dd + '_report.html'

    if dex in f:
        file = filepath + dd + '_report.html'
    else:
        print('还未存在当前日期的测试报告')
        print('开始产生测试报告...')
        report = RunReport()
        cases = report.add_cases()
        report.run_cases_by_beautiful_report(cases)  # 运行报告
        file = filepath + dd + '_report.html'
    return file


# 邮件内容
mail_content = {'subject': '%s接口测试报告' % dd, 'content': 'Dear all,'
                                                       '以上是测试basicservice基础数据服务的一期结果，详情请下载html和logfu附件查看。'
                                                       '（PS:请下载打开，不要在线打开；若html仍无法打开，请重试几次或者联系我。）'
                                                       '开发人员若想定位问题，可复制html报告中的case的【测试方法】到log中查看对应的url、请求头部、请求参数、返回报文。',
                'attachments': get_file()}

# 登陆邮件
e = Environment()
sender = e.get_env('emailSender', 'user')
password = e.get_env('emailSender', 'pwd')
server = zmail.server(sender, password)

# 发送邮件
receivers = e.get_env('emailReceiver', 'receivers')  # 获取接收邮件人
server.send_mail(receivers.split(','), mail_content)
print('发送报告成功')