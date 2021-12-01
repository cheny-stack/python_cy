# -*- coding: utf-8 -*
import re

oldfile = open('C:\\work\\montnets\\5g-ccc\\sql\\5g-ccc.sql', 'r', encoding='UTF-8')
newfile = open('newfile.sql', 'w')
for line in oldfile:
    if not str(line).startswith('DROP TABLE'):
        newfile.write(line)

oldfile.close()
newfile.close()
