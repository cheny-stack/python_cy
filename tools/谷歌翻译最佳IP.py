'''
如果报错：
>>> ModuleNotFoundError: No module named 'win32clipboard'

解决方式：
>>>安装pywin32依赖库,命令行运行:       pip install pywin32
'''

from concurrent.futures import ThreadPoolExecutor
import os
import win32clipboard as clip


def copy(txt):
    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardData(clip.CF_UNICODETEXT, txt)
    clip.CloseClipboard()


def ipList():
    '''获取IP地址'''
    return {i.strip() for i in ips.splitlines() if i.strip()}


def pingInfo(ip):
    '''ping Ip 获取ms 最终取最小值'''
    cmd = f'ping /n 1 {ip}'
    for echoTxt in os.popen(cmd):
        if '请求超时。' in echoTxt:
            ipAndSpeed.append([ip, 9999])
            print(ip, '超时')
            return
        if echoTxt := echoTxt.strip():
            echoTxt = echoTxt.replace(' ', '')
            if '，平均=' in echoTxt:
                ms = int(echoTxt.split('=')[-1].replace('ms', ''))  # 分割平均=xxms
                ipAndSpeed.append([ip, ms])
                print(ip, f'{ms}ms')
                return


def fastScan():
    #使用线程池，设置12个线程，可修改
    with ThreadPoolExecutor(12) as Pool:
        Pool.map(pingInfo, ipList())
        
import fileinput
import re
def replaceHostFile(hostLine):
    domain = hostLine.split(" ")[1]
    # 打开hosts文件，将文件内容读入一个列表
    hosts_path="C:/Windows/System32/drivers/etc/HOSTS"
    with open(hosts_path, 'r', encoding='gb18030', errors='ignore') as file:
        lines = file.readlines()
        # 查找和替换每一行
        for i in range(len(lines)):
            # 查找以“Hello”开头的行
            if re.search(domain, lines[i]):
                # 将该行替换为“Goodbye”
                lines[i] = hostLine
    with open(hosts_path, "w", encoding='gb18030', errors='ignore') as file:
        file.writelines(lines)


if __name__ == '__main__':
    ips = '''
142.250.4.90
172.253.114.90
172.217.203.90
172.253.112.90
142.250.9.90
172.253.116.90
142.250.97.90
142.250.30.90
142.250.111.90
172.217.215.90
142.250.11.90
142.251.9.90
108.177.122.90
142.250.96.90
142.250.100.90
142.250.110.90
172.217.214.90
172.217.222.90
142.250.31.90
142.250.126.90
142.250.10.90
172.217.195.90
172.253.115.90
142.251.5.90
142.250.136.90
142.250.12.90
142.250.101.90
172.217.192.90
142.250.0.90
142.250.107.90
172.217.204.90
142.250.28.90
142.250.125.90
172.253.124.90
142.250.8.90
142.250.128.90
142.250.112.90
142.250.27.90
142.250.105.90
172.253.126.90
172.253.123.90
172.253.122.90
172.253.62.90
142.250.98.90
142.250.185.238
142.251.116.101
216.58.214.14
142.250.189.206
216.58.209.174
142.250.203.142
142.250.218.14
142.251.10.138
142.251.40.174
142.250.185.174
172.217.16.46
172.217.0.46
172.217.31.142
216.58.220.142
172.217.13.142
172.253.113.90
108.177.97.100
108.177.111.90
108.177.125.186
108.177.126.90
108.177.127.90
142.250.1.90
142.250.13.90
142.250.99.90
142.250.102.90
142.250.103.90
142.250.113.90
142.250.114.90
142.250.115.90
142.250.123.90
142.250.138.90
142.250.141.90
142.250.142.90
142.250.145.90
142.250.152.90
142.250.153.90
142.250.157.90
142.250.157.183
142.250.157.184
142.250.157.186
142.250.158.90
142.250.159.90
142.251.1.90
142.251.2.90
142.251.4.90
142.251.6.90
142.251.8.90
142.251.10.90
142.251.12.90
142.251.15.90
142.251.16.90
142.251.18.90
142.251.107.90
142.251.111.90
142.251.112.90
142.251.116.90
142.251.117.90
142.251.120.90
142.251.160.90
142.251.161.90
142.251.162.90
142.251.163.90
142.251.166.90
172.253.58.90
172.253.63.90
172.253.117.90
172.253.118.90
172.253.119.90
172.253.125.90
172.253.127.90
216.58.227.65
216.58.227.66
216.58.227.67
    '''

    os.system('title 查找最佳的谷歌翻译IP - by wkdxz@52pojie.cn')
    ipAndSpeed = []
    print('正在加紧Ping，很快就好，请耐心等待！\n')

    fastScan()
    os.system('cls')  #清屏

    #ip列表排序
    sortedSpeed = sorted(ipAndSpeed, key=lambda x: x[-1])
    for n, i in enumerate(sortedSpeed, 1):
        i[-1] = '超时' if i[-1] == 99999 else f'{i[-1]}ms'
        print(f'【{str(n).zfill(2)}】\t{i[0]}\t {i[1]}')

    #取最佳值
    fastip, ms = sortedSpeed[0]
    hostTxt = f'{fastip} translate.googleapis.com'
    copy(hostTxt)
    replaceHostFile(hostTxt)

    print(f'\n最佳IP是：【{fastip}】，响应时间：【{ms}】')
    print(
        f'\n\n设置hosts的内容“已复制到剪贴板”：   {hostTxt}\n\n\n按【任意键】打开hosts目录，然后【手动】修改。',
        end='')

    # os.system('pause>nul')
    # os.popen('explorer /select,C:\Windows\System32\drivers\etc\hosts')
