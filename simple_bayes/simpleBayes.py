#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def get_data():
    text = ['I fuck and garbage your dog',
            'I like your dog and cats',
            'hello good morigin',
            'hi Bob where your dog I wangt beat them']
    split_text = [x.split() for x in text]
    lable = [1, 0, 0, 1]
    return split_text, lable


def get_unique_data(dataSet):
    """
    :param dataSet: 数据样本[[word], [word], [word]]
    :return: 唯一的单词(全部转换为小写)
    """
    unique_set = set()
    for data_list in dataSet:
        unique_set = unique_set | set([x.lower() for x in data_list])
    return list(unique_set)


def word2Vec(unique_set, inputText:list):
    """
    获取词汇表(unique_set)中有的值, 1 为有, 且位置与单词在表中的位置一样
    :param unique_set: 词汇表
    :param inputText: 输入文档, list
    :return: [0(单词不存在于词汇表), 1(单词存在于词汇表), 0, 1, 1, 0]
    """
    word_exit = [0]*len(unique_set)
    for word in inputText:
        if word in unique_set:
            word_exit[unique_set.index(word)] = 1
    return word_exit


def trainNB0(trainMatrix, trainCategory):
    """
    计算出的是p(label=1的概率) p(当label=1时各个词出现的概率)  p(当label=0时各个词出现的概率)
    :param trainMatrix:
    :param trainCategory:
    :return:
    """
    # 有多少个训练集
    num_of_train = len(trainMatrix)
    # 词汇表有多少单词
    num_of_word = len(trainMatrix[0])
    # 计算label 为 1 的文章的概率
    p_label_equal_1 = sum(trainCategory)/float(num_of_train)

    p0Num = np.zeros(num_of_word) # 在这里将list转换为np.darray , 方便将来计算队列中每个值的商
    p1Num = np.zeros(num_of_word)
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(num_of_train):
        # 当文章标签为1 时, 每个单词出现的概率
        if trainCategory[i] == 1:
            # 将p1Num的值更新为训练集中的值
            p1Num += trainMatrix[i]
            # print(p1Num, "p1Num")  # np.darray() [1, 0, 0, 1] 代表字典中的词共出现过多少次
            # 这个文档共有多少单词在字典中
            p1Denom += sum(trainMatrix[i])
            print(p1Denom, "第{}次".format(i))  # 共有多少个字典中的词出现
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num/p1Denom
    p0Vect = p0Num/p0Denom
    return p0Vect, p1Vect, p_label_equal_1

def getP():
    pass

if __name__ == "__main__":
    split_data, lable = get_data()
    # print(split_data)
    unique_data = get_unique_data(split_data)
    print(unique_data)
    list_of_tran = []
    for i in split_data:
        list_of_tran.append((word2Vec(unique_data, i)))
    print(list_of_tran)
    p0, p1, pA = trainNB0(list_of_tran, lable)
    print(pA, p0, p1)


