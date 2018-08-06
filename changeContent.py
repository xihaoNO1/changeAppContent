#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import random
from PIL import  Image

def addContent():

    # 获取目标路径
    path = sys.path[0]
    print(path)
    print('内容修改中....')
    changeFile(path)
    showComplete()

def showComplete():
    '''显示完成'''
    print ('***************   修改项目完成,可以打包了  ******************')

def changeFile(filepath):
    '''修改文件'''
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            changeFile(fi_d)
        else:
            num = random.randint(0, 100)
            pathStr = os.path.join(filepath, fi_d)
            typeStr = pathStr.split('.')[-1]
            if typeStr == "h":
               with open(pathStr, 'r') as f1:
                   content1 = f1.readlines()
                   index1 = 0
                   if '@end\n' in content1:
                       for i,str in enumerate(content1):
                           if str == '@end\n' or str == '@end':
                               index1 = max(index1,i)

                       content1.insert(index1, "\n" * num)
                       os.remove(pathStr)
                       with open(pathStr, 'w') as f2:
                           f2.writelines(content1)

            elif typeStr == 'm':
               with open(pathStr, 'r') as f3:
                   content2 = f3.readlines()
                   index2 = 0
                   num = random.randint(0, 100)
                   if '@end\n' in content2:
                       for i,str in enumerate(content2):
                           if str == '@end\n' or str == '@end':
                               index2 = max(index2,i)
                       content2.insert(index2, "\n" * num)
                       os.remove(pathStr)
                       with open(pathStr, 'w') as f4:
                           f4.writelines(content2)

            elif typeStr == 'png':
            	
            	# #首先检测图片是否正常
            	# if IsValidImage(pathStr) == False:
            	# 	continue
                try:
                    img = Image.open(pathStr).convert('RGBA')
                except IOError as e:
                    continue

                size = img.size

                '''如果是1024上架图标,重新处理,去掉透明通道'''
                if size == (1024,1024):
                    img = Image.open(pathStr).convert('RGB')
                    os.remove(pathStr)
                    img.save(pathStr, 'PNG')
                else:
                    pix = img.load()
                    for x in range(0, size[0]):
                        for y in range(0, size[1]):
                            r = random.randint(0, 1)
                            pix[x, y] = (pix[x, y][0] - r, pix[x, y][1], pix[x, y][2], pix[x, y][3])
                    os.remove(pathStr)
                    img.save(pathStr, 'PNG')

#                    img = Image.open(pathStr).convert('RGB')
#                    size = img.size
#                    pix = img.load()
#                    for x in range(0, size[0]):
#                        for y in range(0, size[1]):
#                            r = random.randint(0, 1)
#                            pix[x, y] = (pix[x, y][0] - r, pix[x, y][1], pix[x, y][2])
#                    img.save(pathStr, 'PNG')


'''检测图片是否完整'''
def IsValidImage(pathfile):
    bValid = True
    try:
        Image.open(pathfile).verify()
    except:
        print(pathfile)
        bValid = False
    return bValid

def deleteContent():
    '''还原添加和修改的内容'''
    # 强制还原
    os.system('git reset --hard')
    print ('***************   还原项目完成  ******************')


if __name__ == '__main__':
    type = input('请输入需要进行的操作'
                     ' (a 修改工程;'
                     'd 还原工程) : ')

    if type == 'a':
        '''添加内容'''
        addContent()

    elif type == 'd':
        '''还原内容'''
        deleteContent()
