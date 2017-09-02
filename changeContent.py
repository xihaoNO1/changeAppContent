#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import re
import sys
import random

def addContent():
    '''添加垃圾文件'''

    # 更改xcode文件引用
    from pbxproj import XcodeProject

    # 定义类名list
    classList = []

    # 获取全部字母
    letterlist = [chr(i) for i in range(97, 123)]  # 所有小写字母

    for i in range(classNum):
        className = ''
        for j in range(classNameLen):
            classChr = letterlist[random.randint(0, 25)]
            className = className + classChr
        className = className + str(i)
        classList.append(className)

    # 获取目标路径
    path = sys.path[0]
    print path

    # 获取需要打开的工程
    projectPath = path + '.xcodeproj/project.pbxproj'
    # #定义类中的属性
    propertyName = ''
    for i in range(10):
        classChr = letterlist[random.randint(0, 10)]
        propertyName = propertyName + classChr

    # 打开工程
    project = XcodeProject.load(projectPath)

    print '内容修改中....'

    # 循环生成文件夹
    for filePath in classList:
        '''创建文件夹,在文件夹中添加.h .m 文件'''
        os.mkdir(filePath)
        # 在文件夹中添加 .h .m文件
        with open(path + '/' + filePath + '/' + filePath + '.h', 'w') as f:

            f.write('\n\n#import <Foundation/Foundation.h>\n@interface %s : NSObject\n@property(nonatomic,copy)NSString *%s;\n@end\n' %
                    (filePath, propertyName))

        with open(path + '/' + filePath + '/' + filePath + '.m', 'w') as f2:
            addContent = ''
            for i in range(1000):
                num = random.randint(0, 10)
                addContent = addContent + str(num)

            f2.write(
                '\n\n#import "%s.h"\n@implementation %s\n- (instancetype)init{\nself = [super init];\n if (self) {\n   }\nreturn self;\n}'
                '\n- (NSString *)%s{\nreturn @"%s";\n}\n@end\n' %
                (filePath, filePath, propertyName, addContent))
        project.add_folder(path + '/' + filePath)

    project.save()
    print '***************   修改工程完成,可以打包了  ******************'


def deleteContent():
    '''删除添加的垃圾文件'''
    #先进行强制还原
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

    # 定义需要添加的类的数量
    classNum = 100
    # 定义类名中字母的长度
    classNameLen = 15

    if type == 'a':
        '''添加垃圾文件'''
        addContent()

    elif type == 'd':
        '''删除垃圾文件'''
        deleteContent()










