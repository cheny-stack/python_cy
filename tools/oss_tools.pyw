# -*- coding: utf-8 -*-
import oss2
from PIL import ImageGrab, Image
import time
import pyperclip
# pip install --index-url https://pypi.tuna.tsinghua.edu.cn/simple/ pyperclip
auth = oss2.Auth('LTAI4GF4KdU9N4aJkG9hKMfq', 'BQ5WPZYo24a2HGtqxSfMtawxh8pMay')
bucket = oss2.Bucket(auth, 'https://oss-cn-beijing.aliyuncs.com', 'b-ccy')
path = "D:/temp/"


# 将当前时间转换为时间字符串，默认为2017-10-01 13:37:04格式
def now_to_date(format_string="%Y%m%d%H%M%S"):
    time_stamp = int(time.time())
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date


def get_file_from_clipboard(file_path):
    im = ImageGrab.grabclipboard()
    if isinstance(im, Image.Image):
        im.save(file_path)
        return True
    return False


def to_oss(file_name, file_path):
    result = bucket.put_object_from_file('oss-file/' + file_name, file_path)
    # HTTP返回码。
    print('http status: {0}'.format(result.status))
    if result.status == 200:
        url = result.resp.response.url
        return url
    return None


file_name = now_to_date() + ".png"
file_path = path + file_name
if get_file_from_clipboard(file_path):
    url = to_oss(file_name, file_path)
    if url is not None:
        print('url: {0}'.format(url))
        pyperclip.copy(url)
    else:
        print("失败")
else:
    print("未读取到剪切板图片")
