# -*- coding:utf-8 -*-
'''
Created on 2015年11月20日

@author: YinongLong

用来计算相似性的模块
'''

class Similarity:
    
    def __init__(self, itemSet=None):
        '''
        初始化对象的时候，需要输入需要计算相似性的物品的集合
        '''
        self.dataSet = itemSet
        # 存储相似性矩阵
        self.simiMat = dict()
        
    def itemSimilarity(self):
        '''
        计算通过电影的类别标签来计算电影之间的相似度
        '''
        if self.dataSet == None:
            return None
        for item, geSet in self.dataSet.items():
            self.simiMat[item] = dict()
            for otherItem, othergeSet in self.dataSet.items():
                if item == otherItem:
                    continue
                interSe = geSet & othergeSet
                unionSe = geSet | othergeSet
                self.simiMat[item][otherItem] = len(interSe) / (1.0 * len(unionSe))
        return self.simiMat