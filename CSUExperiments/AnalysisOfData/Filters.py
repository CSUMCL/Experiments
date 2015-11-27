# -*- coding:utf-8 -*-
'''
Created on 2015年11月12日

@author: YinongLong
'''
from datetime import datetime

class Filetrs:
    
    def filterInstances(self, dataSet, num = 10):
        '''
        从指定的数据集过滤数据，选择num个数据
        :param dataSet: 待过滤的数据集
        :type dataSet: list
        :param saveFile: 将过滤结果存放的文件
        :type saveFile: string
        :param num: 返回过滤的结果数
        :type num: integer
        :return examples: [['user1','id1', 'rating', 'stamp', 'easydate'], ..]
        '''
        sortedDataSet = sorted(dataSet, key = lambda x: int(x[0]))
        currentUser = None
        tempList = []
        temp_result = []
        index = dict()
        for item in sortedDataSet:
            if item[0] != currentUser:
                currentUser = item[0]
                if len(tempList) > 0:
                    # 对某一个用户按照其观影时间排序，并将其用户名与时间跨度记入字典
                    sortList = sorted(tempList, key = lambda x: int(x[-1]))
                    timeLength = abs(sortList[-1][-1] - sortList[0][-1])
                    index[sortList[0][0]] = timeLength
                    temp_result.extend(sortList)
                tempList = []
            item[-1] = int(item[-1])
            tempList.append(item)
        # 对用户名－观影跨度字典按照跨度的大小从大到小排序，并且选取前num个
        sortedDictList = sorted(index.items(), key = lambda x: x[1], reverse = True)
        otherIndex = dict(sortedDictList[0:num])
        result = []
        for item in temp_result:
            if item[0] in otherIndex:
                # 给每一个观影记录后面添加易读的时间日期形式
                easyReadDate = datetime.fromtimestamp(item[-1])
                item.append(str(easyReadDate))
                result.append(item)
        return result
    
    def generateUserWithMovie(self, dataset):
        '''
        根据选出的特征用户数据集，过滤出该用户在每个月份所点评的具体电影ID
        :param dataset: 选出来的特征用户的数据集
        :type dataset: list
        :return examples: {'user1':{'199809':set(['id1','id2']), ..}, ..}
        '''
        result = dict()
        currUser = None
        currYear = None
        currMont = None
        for item in dataset:
            time = item[-1].strip().split('-')
            if item[0] != currUser:
                currUser = item[0]
                currYear = time[0]
                currMont = time[1]
                result[currUser] = dict()
                result[currUser][currYear+currMont] = set()
                result[currUser][currYear+currMont].add(item[1])
            else:
                if time[0] == currYear and time[1] == currMont:
                    result[currUser][currYear+currMont].add(item[1])
                else:
                    currYear = time[0]
                    currMont = time[1]
                    result[currUser][currYear+currMont] = set()
                    result[currUser][currYear+currMont].add(item[1])
        return result
    
    def filterForGraph(self, dataset):
        '''
        通过给出的已经筛选出来的特征用户的数据，来过滤生成绘图的数据
        生成的绘图数据以字典的形式返回
        :param dataset: 筛选出来的特征用户数据集
        :type dataset: list
        :return examples:{'user1':{'199809':n1, ..}, ..}
        '''
        result = dict()
        currUser = None
        currYear = None
        currMont = None
        count = 0
        for item in dataset:
            time = item[-1].strip().split('-')
            if currUser != item[0]:
                if currUser != None:
                    result[currUser][currYear+currMont] = count
                currUser = item[0]
                currYear = time[0]
                currMont = time[1]
                count = 1
            else:
                if time[0] == currYear and time[1] == currMont:
                    count += 1
                else:
                    if currUser not in result:
                        result[currUser] = dict()
                    result[currUser][currYear+currMont] = count
                    currYear = time[0]
                    currMont = time[1]
                    count = 1
        return result
    
    def moviesWithGenre(self, movieDataset, genreDataset):
        '''
        根据电影信息文件以及类别文件，生成一个电影及其类别标签的字典返回，
        其中的字典是以电影编号为key，以该电影的类型标签的集合为value
        :return examples: {'movie1':set(['tag1', ..]), ..}
        '''
        genreDict = dict()
        result = dict()
        for item in genreDataset:
            if item[0] != None and item[0] != '':
                genreDict[item[1]] = item[0]
        for item in movieDataset:
            if len(item) == 0:
                return None
            result[item[0]] = set()
            for posi in xrange(-1, -20, -1):
                state = item[posi]
                if state == '1':
                    genre = genreDict[str(posi + 19)]
                    result[item[0]].add(genre)
        return result