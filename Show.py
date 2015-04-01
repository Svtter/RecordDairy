#!/usr/bin/env python
# coding: UTF-8

__author__ = "svitter"

'''
Record my daily life and print
'''

import datetime


# 单项
class Item:
    '''
    项目基类，用于所有任务项的集成
    '''
    def __init__(self, startDate, frequent, gross,
                 curPage, name, **kw):
        '''
        条目基础类

        startDate = datetime.datetime(2015, x, x)
        item = new Item(startDate, 30, 30, 400, 'Algorithm', curPage = 30)

        '''
        self.startDate = startDate
        self.frequent = frequent
        self.curPage = curPage
        self.gross = gross
        self.name = name
        self.subItem = kw.get('subItem')

    def delay(self, day):
        '''
        推迟时间

        ex: 将开始时间推迟3天
        item.delay(3)
        静态的初始化，目前没有效果，仅能单纯计算
        '''
        self.startDate = self.startDate + datetime.timedelta(day)

    def numofDays(self):
        '''
        剩余的时间
        '''
        return (datetime.datetime.now() - self.startDate).days

    def showStatus(self):
        '''
        输出当前项目的状态
        '''
        print "-----------------------------------------------"
        print "Name: ", self.name
        print "开始时间:", self.startDate
        print "结束时间:", self.endDate()
        print "当前应阅读页数:", self.shouldPage()
        percent = (self.shouldPage() / float(self.gross) * 100)
        print "完成百分比:", "%.2lf" % percent + '%'

    def endDate(self):
        '''
        返回结束时间

        >>>self.endDate()
        2015-03-13

        '''
        rest = (self.gross - self.curPage) / self.frequent
        return self.startDate + datetime.timedelta(rest)

    def shouldPage(self):
        '''
        应阅读到的页数
        '''
        return self.numofDays() * self.frequent + self.curPage


# 算法类，可以参数化
class Algorithm(Item):
    '''
    算法具体类

    没有配置文件，暂时写在类中
    '''
    wholePage = 480
    curPage = 37
    frequent = 10
    startDate = datetime.datetime(2015, 3, 17)

    @staticmethod
    def getstandardAlgorithm():
        '''
        返回普通变量
        '''
        return Algorithm(Algorithm.startDate, Algorithm.frequent,
                         Algorithm.wholePage, Algorithm.curPage, 'Algorithm')


# 日常检查类
class DailyCheck:
    '''
    按日检查类
    '''
    def __init__(self):
        pass

    @staticmethod
    def Show(Item):
        '''
        show all check
        '''
        for x in Item:
            x.showStatus()

    @staticmethod
    def dayCheck():
        '''
        check whether the day is sunday, to make a summary
        '''
        print ""
        if datetime.date.today().weekday() == 6:
            print "It's Sunday, you might need to write summary."

# main
item = []
item.append(Algorithm.getstandardAlgorithm())
DailyCheck.Show(item)
DailyCheck.dayCheck()
