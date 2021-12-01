# -*- coding: utf-8 -*
from subprocess import call

from PyQt5.QtWidgets import *

app = QApplication([])
clipboard = app.clipboard()

# 当剪切板变动会执行该方法
def change_deal():
    # os.system('python C:\\work\\Python\\PycharmProjects\\python_cy\\tools\\readaload_by_edge.py')
    call(["python","C:\\work\\Python\\PycharmProjects\\python_cy\\tools\\readaload_by_edge.py"])


# 监听剪切板变动 alt_click
clipboard.dataChanged.connect(change_deal)
app.exec_()
