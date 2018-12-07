import os


def write_log(app, casename):
    file = os.path.join(os.path.dirname(os.getcwd()), f'logs/{casename}.log')
    print(file)
    cmd = f'adb shell logcat -v time | grep {app} > {file}'
    print(cmd)
    log = os.system(cmd)