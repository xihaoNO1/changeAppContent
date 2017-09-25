#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
path = input('请输入仓库地址:')
os.chdir(path)
list = os.popen('git branch','r').read()
list = list.splitlines()
for branch in list:
    os.system('git checkout %s' % branch)
    os.system('git pull')