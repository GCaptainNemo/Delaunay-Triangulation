#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 11360
# datetime： 2021/3/18 23:31 

# delaunay triangulation scipy version

from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

class DT:
    def __init__(self):
        ...

    def make_data(self):
        """
        使用iris数据集测试Graham-scan算法的鲁棒性，注意数据中有重复的点
        :return:
        """
        iris = load_iris()
        data = iris.data
        self.points = data[:50, :2]
        temp_index = 0
        for point in self.points:
            plt.scatter(point[0], point[1], marker='o', c='y')
            index_str = str(temp_index)
            plt.annotate(index_str, (point[0], point[1]))
            temp_index = temp_index + 1

    def delaunay(self):
        tri = Delaunay(self.points)
        plt.triplot(self.points[:, 0], self.points[:, 1], tri.simplices.copy())
        plt.plot(self.points[:, 0], self.points[:, 1], 'o')
        plt.show()


if __name__ == "__main__":
    a = DT()
    a.make_data()
    a.delaunay()


