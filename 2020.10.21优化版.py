# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:24:56 2020

@author: admin
"""

'''
程序的实现思路再调整一下，条件分支的层级太多，不好
'''

import random
n=random.randint(0, 100)
print(n)
try:
    m=eval(input('请输入一个0到100的整数:'))    # 你的目的是要转化为整数，不用eval
    if type(m)==int:    # 这个用法也不好，不需要判断类型，只需要进行转化即可
        if m < 100 and m > 0:    # 把这个条件判断放到循环里面
            count=1
            while m != n:   # 这里的条件和下面的，有点乱。并且，程序能满足多次输入吗？
                if m != n:    
                    if m > n:
                        print("你猜的也太大了")
                        m=eval(input('请再输入一个0到100的整数:'))
                    
                    else:
                        print("你猜的数字有点小啊")
                        m=eval(input('请再输入一个0到100的整数:'))
                    count+=1
            else:
                if count == 1:
                    print("竟然真的有人能一次就猜对，兄弟买彩票去吧")
                elif  count < 10:
                    print("你只猜了{}次就猜对了？".format(count))
                else:
                    print("不会真的有人要猜{}次才对吧！".format(count))
        else:
            print("要输入的是0到100啊！！！读题认真一点好不好")
            print("请仔细读题后重新启动")
    else:
        print("要输入一个整数啊！整！数！！！")
        print("请仔细读题后重新启动吧")
except:
    print("你输入的是整数嘛？？OWO")
    print("请仔细读题后重新启动吧")
