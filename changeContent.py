#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import re
import sys
import random
# 更改xcode文件引用
from mod_pbxproj import XcodeProject


def addContent():
    '''添加垃圾文件'''
    # 获取全部字母
    letterlist = [chr(i) for i in range(97, 123)]  # 所有小写字母

    # 获取目标路径
    path = sys.path[0]
    print path

    #定义类中的属性
    for i in range(classNameLen):
        global propertyName
        classChr = letterlist[random.randint(0, 20)]
        propertyName = propertyName + classChr


    print '内容修改中....'
    changeFile(path)
    addFiles(path)

def addFiles(dirPath):
    '''添加文件'''
    # 获取需要打开的工程
    projectPath = dirPath + '.xcodeproj/project.pbxproj'
    # 打开工程
    project = XcodeProject.Load(projectPath)

    letterlist = [chr(i) for i in range(97, 123)]  # 所有小写字母
    # 定义类名list
    classList = []
    for i in range(classNum):
        className = ''
        for j in range(classNameLen):
            classChr = letterlist[random.randint(0, 25)]
            className = className + classChr
        className = className + str(i)
        classList.append(className)

    # 循环生成文件夹
    for filePath in classList:
        '''创建文件夹,在文件夹中添加.h .m 文件'''
        os.mkdir(filePath)
        # 在文件夹中添加 .h .m文件
        with open(dirPath + '/' + filePath + '/' + filePath + '.h', 'w') as f:

            f.write('\n\n#import <Foundation/Foundation.h>\n@interface %s : NSObject\n@property(nonatomic,copy)NSString *%s;\n@end\n' %
                    (filePath, propertyName))

        with open(dirPath + '/' + filePath + '/' + filePath + '.m', 'w') as f2:
            addContent = ''
            for i in range(100):
                num = random.randint(0, 10)
                addContent = addContent + str(num)

            f2.write(
                '\n\n#import "%s.h"\n@implementation %s\n- (instancetype)init{\nself = [super init];\n if (self) {\n   }\nreturn self;\n}'
                '\n- (NSString *)%s{\nreturn @"%s";\n}\n@end\n' %
                (filePath, filePath, propertyName, addContent))
        project.add_folder(dirPath + '/' + filePath)

    project.save()
    print '***************   修改工程完成,可以打包了  ******************'

def changeFile(filepath):
    '''修改文件'''
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            changeFile(fi_d)
        else:

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

                        content1.insert(index1, "@property(nonatomic,copy)NSString *%s;\n" % propertyName)
                        content1.insert(0, "#import <Foundation/Foundation.h>\n")
                        with open(pathStr, 'w') as f2:
                            f2.writelines(content1)

            elif typeStr == 'm':
                with open(pathStr, 'r') as f3:
                    content2 = f3.readlines()
                    index2 = 0
                    if '@end\n' in content2:
                        addContent = ''
                        for i in range(100):
                            num = random.randint(0, 10)
                            addContent = addContent + "%s"%num

                        for i,str in enumerate(content2):
                            if str == '@end\n' or str == '@end':
                                index2 = max(index2,i)
                        content2.insert(index2, "\n- (NSString *)%s{\nreturn @\"%s\";\n}\n" % (propertyName, addContent))
                        content2.insert(0, "#import <Foundation/Foundation.h>\n")
                        with open(pathStr, 'w') as f4:
                            f4.writelines(content2)

            elif typeStr == 'png':
                pass



def deleteContent():
    '''删除添加的垃圾文件'''
    # 先进行强制还原
    os.system('git reset --hard')
    filepath = sys.path[0]
    #列出文件夹
    pathList = os.listdir(filepath)
    #筛选需要删除的文件夹,构建正则表达式
    rex = '^[a-z]{%s}[0-9]+$' % classNameLen
    pathList = [x for x in pathList if re.match(rex,x) != None]

    for x in pathList:
        floderPath = sys.path[0]+'/'+x
        os.system('rm -rf %s' % floderPath)

    print '***************   数据还原完成  ******************'


if __name__ == '__main__':
    type = raw_input('请输入需要进行的操作'
                     ' (a 添加内容;'
                     'd 删除内容) : ')

    propertyName = ''

    # 定义需要添加的类的数量
    classNum = 500
    # 定义类名中字母的长度
    classNameLen = 20

    if type == 'a':
        '''添加垃圾文件'''
        addContent()

    elif type == 'd':
        '''删除垃圾文件'''
        deleteContent()










