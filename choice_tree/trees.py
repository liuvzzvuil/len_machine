#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
程序构建详情参考《机器学习实战》第三章, 决策树
"""

from math import log
import numpy as np
import collections
import operator



def calaShannonEnt(dataSet):
    """
    计算香农熵
        信息: 如果待分类的事务可能划分在多个分类之中，则符号x i 的信息定义为 -math.log(P(x_i), 2)
        为了计算熵，我们需要计算所有类别所有可能值包含的信息期望值 -∑(i=1, n)P(x_i)(log2(P(x_i)))

    创建一个数据字典，它的键值是最后一列的数值 。如果当前键值不存在，则扩展字典并将当前键值加入字典。每个键值都记录了当前类别出现的次数。最后，使用所有类标
    签的发生频率计算类别出现的概率
    :param dataSet:
    :return:
    """
    num_item = len(dataSet)
    # np_num_item = np.array(dataSet)
    item_num_list = [x[-1] for x in dataSet]
    # item_num_list = np_num_item[:, 2]
    # print(item_num_list)
    count_dic = dict(collections.Counter(item_num_list))
    shannonEnt = 0.0
    list_prond = [x/num_item for x in count_dic.values()]
    for i in list_prond:
        shannonEnt -= i * log(i, 2)
    return shannonEnt


def splitDataSet(dataSet: "待划分的数据集", spa: "划分数据集的特征(即数据的位置)", tag: "需要返回的特征的值"):
    """
    :param dataSet: 待划分的数据集
    :param spa: 划分数据集的特征
    :param tag: 需要返回的特征的值
    :return:

    # 数据集这个列表中的各个元素也是列表，我们要遍历数据集中的每个元素，一旦发现符合要求的值，则将其添加到新创建的列表中
    获取与所选特征联合出现的特征!!
    """
    reDataSet = []
    for data in dataSet:
        if data[spa] == tag:
            reduce = data[:spa]
            reduce.extend(data[spa+1:])
            reDataSet.append(reduce)
    return reDataSet


# 接下来我们将遍历整个数据集，循环计算香农熵和 splitDataSet() 函数，找到最好的特征划分方式。熵计算将会告诉我们如何划分数据集是最好的数据组织方式
def chooseBestSetInLoop(dataSet):
    """
    :param dataSet: 数据需要满足一定的要求：一: 数据必须是由列表组成的列表，而且所有的列表元素都要具有相同的长度；二: 数据的最后一列或者每个实例的最后一个元素是当前实例的类别标签
    :return:
    """
    # 计算原始数据集的 香农熵
    len_of_spa = len(dataSet[0])-1
    raw_entropy = calaShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestSpa = -1
    temp = 100000
    for i in range(len_of_spa):
        # 每个特征, 可能有哪些值, 存储在唯一集合中, 确保在重新划分数据集时不会出现如 **NULL_VALUE** 位置所指出的问题
        featlist = [x[i] for x in dataSet]
        uniquefead = set(featlist)
        newEntropy = 0.0
        for value in uniquefead:
            # 循环获取符合要求的数据集(与某些特征(i, value)联合出现的特征数据集)
            comSpaDataSet = splitDataSet(dataSet, i, value)  # combination 组合  组合出现的特征的数据集
            prob = len(comSpaDataSet)/float(len(dataSet))
            # print(calaShannonEnt(comSpaDataSet), comSpaDataSet)
            newEntropy += prob*calaShannonEnt(comSpaDataSet)
            # print(newEntropy, comSpaDataSet, i, value)
        # 熵越小越好 为什么需要计算原始数据集的熵? 防止熵出现负数么? 最小就是0 (不会出现负数)
        # infoGain = raw_entropy - newEntropy
        # if infoGain > bestInfoGain:
        #     bestInfoGain = infoGain
        #     bestSpa = i
        if newEntropy < temp:
            temp = newEntropy
            bestSpa = i
    return bestSpa


def get_labels(data_list):
    dataCount = collections.Counter(data_list)
    return dataCount.most_common(1)[0][0]


def createTree(dataSet, labels):
    data_list = [x[-1] for x in dataSet]
    data_set = set(data_list)
    if len(dataSet) == 1:
        return dataSet[0]
    if len(dataSet) == 1:
        # 当dataSet只有1个(遍历完全部特征时), 返回特征最多的
        return get_labels(data_list)
    bestFeat = chooseBestSetInLoop(dataSet)
    bestLabel = labels[bestFeat]
    choice_tree = {bestLabel: {}}
    del(labels[bestFeat])
    featValues = [x[bestFeat] for x in dataSet]
    # print(featValues)
    uniqueValue = set(featValues)
    for value in uniqueValue:
        subLabels = labels[:]
        choice_tree[bestLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return choice_tree


if __name__ == '__main__':
    dataSet = [[1, 1, 2, 'y'], [1, 1, 3, 'y'], [0, 1, 2, 'n'], [1, 0, 3, 'n'], [1, 0, 2, 'n'], [1, 1, 0, 'm']]
    # print(calaShannonEnt(dataSet))
    # for i in range(3):
    #     print(splitDataSet(dataSet, i, 1), "***{}***".format(i))
    # 从上面的输出可以看出, splitDataSet(重新划分数据集)的作用是: 确定某个位置(特征)的特征值(值), 获取原始数据集中符合要求的数据
    # 亦即: 获取与所选特征联合出现的特征!!
    # [[1, 2, 'y'], [1, 3, 'y'], [0, 3, 'n'], [0, 2, 'n'], [1, 0, 'm']] ***0***  获取到的是原始集合中位置1值为1 的数据
    # [] ***2*** 可以看到, 最后一个特征值只有 0, 2, 3 没有1 , 所以没有符合特征的数据集  **NULL_VALUE**
    # print(chooseBestSetInLoop(dataSet))
    # labels 只要是可迭代对象即可, 元素与特征对应
    print(createTree(dataSet, ['A', 'B', 'C']))
    # get_labels(['y', 'y', 'n', 'n', 'n'])