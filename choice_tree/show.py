#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

desisionNode = {"boxstyle": "sawtooth", 'fc': '0.8'}
leafNode = {"boxstyle": "round4", "fc": '0.8'}
arrow_arg = {"arrowstyle": "<-"}


def createNode():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createNode.ax1 = plt.subplot(111, frameon=False)
    plotNode('testA', (0.5, 0.1), (0.1, 0.5), desisionNode)
    plotNode('testB', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createNode.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction', xytext=centerPt, textcoords='axes fraction', va='center', ha='center', bbox=nodeType, arrowprops=arrow_arg)


if __name__ == "__main__":
    createNode()
