#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
path = input('请输入仓库地址:')
os.chdir(path)
list = os.popen('git branch','r').read()
print(list)
list = list.splitlines()
for branch in list:
    os.system('git checkout %s' % branch)
    os.system('git pull')