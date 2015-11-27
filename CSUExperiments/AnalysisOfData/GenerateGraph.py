# -*- coding:utf-8 -*-
'''
Created on 2015年11月17日

@author: YinongLong

绘制挑选出的用户其看电影的历史图，横坐标表示不同的用户，纵坐标表示月份，
在用户与月份的交点处绘制圆形，圆形的大小表示该月份用户给出电影评分的数量的多少。

数据集是从1997-09-19开始，到1998-04-22收集数据，历时7个月
因此纵轴7个标签点，横轴的标签个数与用户数相同

'''
import numpy as np
import matplotlib.pyplot as plt

class Graph:
    
    def __init__(self):
        self.monthNum = 8
        self.months = [1, 2, 3, 4, 5, 6, 7, 8]
        self.first_mon = ['09', '10', '11', '12']
        self.second_mon = ['01', '02', '03', '04']
    
    def showGraph(self, dataDict):
        '''
        根据所给的数据字典，生成图表表示
        '''
        X = []
        Y = []
        radius = []
        count = 1
        userTags = list()
        for user_tuple in dataDict.items():
            userTags.append(user_tuple[0])
            monData = user_tuple[1]
            ratingNum = self.__getNumByMonth(monData)
#             print ratingNum
#             break
            radius.extend(ratingNum)
            X.extend([count]*self.monthNum)
            Y.extend(self.months)
            count += 1
        colors = np.random.rand(count - 1)
        colo = []
        for item in colors:
            colo.extend([item] * self.monthNum)
        area = np.pi * (15 * np.array(radius))**2
        x = np.array(X)
        y = np.array(Y)
        plt.scatter(x, y, s=area, c=np.array(colo), alpha=0.5)
        xindex = [x for x in xrange(1, len(userTags)+1)]
        
        plt.xticks(xindex, userTags)
        plt.yticks(self.months, self.__getMonthsTags(self.months))
        plt.title(u'影评图')
        plt.show()
        
    def __getMonthsTags(self, monthsList):
        '''
        生成月份标签
        '''
        result = list()
        for month in monthsList:
            actMonth = (month + 8) % 13
            date = '97-' + str(actMonth)
            if actMonth < 9:
                actMonth += 1
                date = '98-' + '0' + str(actMonth)
            result.append(date)
        return result
        
    def __getNumByMonth(self, dictData):
        '''
        对字典里面用户的影评月份及次数根据时间排序，按照如下的时间顺序返回每月的影评数
        如果，该月份不在字典中，则对应月份位置为0
        其中数字1-8分别表示，97年9月、97年10月、97年11月、97年12月
        98年1月、98年2月、98年3月、98年4月
        '''
        first_year = []
        second_year = []
        for item in dictData.items():
            if item[0][-3] == '7':
                first_year.append(item)
            else:
                second_year.append(item)
        fir_year_dict = dict(first_year)
        sec_year_dict = dict(second_year)
#         print fir_year_dict
#         print sec_year_dict
        for item in self.first_mon:
            date = '1997' + item
            if date not in fir_year_dict:
                fir_year_dict[date] = 0
        for item in self.second_mon:
            date = '1998' + item
            if date not in sec_year_dict:
                sec_year_dict[date] = 0
        sorted_fir = sorted(fir_year_dict.items(), key=lambda x: int(x[0][-2:]))
        sorted_sec = sorted(sec_year_dict.items(), key=lambda x: int(x[0][-2:]))
        result = []
        for item in sorted_fir + sorted_sec:
            result.append(item[1])
        resultSum = float(sum(result))
        re = [x/resultSum for x in result]
        return re
        
            