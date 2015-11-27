# -*- coding:utf-8 -*-
'''
Created on 2015年11月21日

@author: YinongLong

'''

class Evaluation:
    
    def contentSimi(self, watchingRecord, simiMat):
        '''
        根据某一个具体用户的影评记录和电影的相似度矩阵，计算用户在每一个
        时间点，受到电影内容相似性影响的指数
        :param watchingRecord: 某一个用户的影评记录
        :type watchingRecord: set
        :param simiMat: 电影的相似度矩阵
        :type simiMat: dict
        '''
#         for item in watchingRecord:
            