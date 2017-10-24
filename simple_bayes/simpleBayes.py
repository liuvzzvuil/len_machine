#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_data():
    text = ['i fuck and garbage your dog', 'i like your dog and cats', 'hello, good morigin', 'hi, Bob , where your dog ? I wangt beat them!']
    split_text = [x.split() for x in text]
    lable = [1, 0, 0, 1]
    return split_text, lable


def get_unique_data(dataSet):
    """
    :param dataSet: 数据样本[[word], [word], [word]]
    :return: 唯一的单词
    """
    unique_set = set()
    for data_list in dataSet:
        unique_set = unique_set | set(data_list)
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


if __name__ == "__main__":
    split_data, lable = get_data()
    unique_data = get_unique_data(split_data)
    print(word2Vec(unique_data, ['dog', 'world']))

