# -*- coding:utf-8 -*-
'''
Created on 2015年11月12日

@author: YinongLong
'''

class DealFiles:
    
    def loadData(self, dataPath, separator='\t'):
        '''
        从指定的路径载入数据，存储为列表类型
        :return examples:[['..'],['..']..]
        '''
        result = []
        datafile = open(dataPath)
        for line in datafile:
            lineEles = line.strip().split(separator)
            result.append(lineEles)
        datafile.close()
        return result
    
    def outputFileWithDate(self, dataSet, filePath):
        '''
        将指定的用户影评数据数据集dataSet（列表），添加易读的时间格式存入指定的文件
        '''
        saveFile = open(filePath, 'w')
        for item in dataSet:
            tempLine = ''
            for ele in item:
                tempLine += str(ele) + '\t'
            tempLine += '\n'
            saveFile.write(tempLine)
        saveFile.close()
        
    def outputFileAboutMovie(self, moviesSet, filepath):
        '''
        将关于电影信息的字典输出表示
        '''
        savefile = open(filepath, 'w')
        for mv, genresSet in moviesSet.items():
            line = mv + '|||'
            for genre in genresSet:
                line += genre + '*'
            line += '\n'
            savefile.write(line)
        savefile.close()
                