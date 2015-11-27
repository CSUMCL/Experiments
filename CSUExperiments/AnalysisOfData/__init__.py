# -*- coding:utf-8 -*-

import DealFiles
import Filters
import GenerateGraph
import Similarity

def main():
    
    # 创建处理文件和数据过滤器对象
    fileOperator = DealFiles.DealFiles()
    filters = Filters.Filetrs()
    dataSet = fileOperator.loadData('/Users/YinongLong/dataSet/ml-100k/u.data')
    result = filters.filterInstances(dataSet, num=15)
#     fileOperator.outputFileWithDate(result, '/Users/YinongLong/dataSet/sortedData')
#     featureData = fileOperator.loadData('/Users/YinongLong/dataSet/sortedData')
    dictGraphData = filters.filterForGraph(result)
#     usersRecord = filters.generateUserWithMovie(result)
    
    graph = GenerateGraph.Graph()
    graph.showGraph(dictGraphData)

    # 读取电影信息文件以及类别标签文件，生成电影以及相对应的标签集合的字典
#     movieDataset = fileOperator.loadData('/Users/YinongLong/dataSet/ml-100k/u.item', '|')
#     genreDataset = fileOperator.loadData('/Users/YinongLong/dataSet/ml-100k/u.genre', '|')
#     movieWithGe = filters.moviesWithGenre(movieDataset, genreDataset)
#     fileOperator.outputFileAboutMovie(movieWithGe, '/Users/YinongLong/dataSet/movieData')
#     
#     # 计算返回电影内容（根据电影类别标签进行的计算）相似度矩阵
#     similarity = Similarity.Similarity(movieWithGe)
#     siMat = similarity.itemSimilarity()
#     print siMat['27']['28']
#     print dictGraphData
if __name__ == '__main__':
    main()