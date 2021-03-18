#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： 11360
# datetime： 2021/3/19 0:13 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


class GrahamScan:
    def __init__(self):
        """寻找一个点集V的凸包CH(V)的算法，时间复杂度O(NlogN)"""
        self.make_data()

    def make_data(self):
        """
        使用iris数据集测试Graham-scan算法的鲁棒性，注意数据中有重复的点
        :return:
        """
        iris = load_iris()
        data = iris.data
        points = data[:50, :2]
        temp_index = 0
        for point in points:
            plt.scatter(point[0], point[1], marker='o', c='y')
            index_str = str(temp_index)
            plt.annotate(index_str, (point[0], point[1]))
            temp_index = temp_index + 1
        results = self.graham_scan(points)

    def graham_scan(self, points):
        """
        graham扫描法计算凸包
        :param points: 处理的数据点
        :return: 凸包顶点(逆时针排列)构成的栈
        """
        index = self.find_init_point(points)
        plt.scatter(points[index, 0], points[index, 1], marker='o', c='r')
        # plt.show()
        data_lst = points.tolist()
        stack = []
        stack.append(data_lst.pop(index))
        origin_point = stack[0]
        # function = lambda x: (np.array([x]) - np.array([origin_point])) @ \
        #                       np.array([[1, 0]]).T / np.linalg.norm(np.array([x]) -
        #                                               np.array([origin_point]))
        # data_lst.sort(key=function)
        data_lst = self.sort_polar_angle_cos(data_lst, origin_point)
        stack.append(data_lst[0])
        stack.append(data_lst[1])
        # print(data_lst)
        for i in range(2, len(data_lst)):
            next_top = np.array([stack[- 2]])
            top = np.array([stack[-1]])
            new_points = np.array([data_lst[i]])
            v1 = np.append(new_points - top, 0)
            v2 = np.append(top - next_top, 0)
            while np.cross(v2, v1)[2] <= 0:
                stack.pop()
                next_top = np.array([stack[- 2]])
                top = np.array([stack[- 1]])
                v1 = np.append(new_points - top, 0)
                v2 = np.append(top - next_top, 0)
            stack.append(data_lst[i])
        print("stack = ", stack)
        length = len(stack)
        for i in range(0, length - 1):
            plt.plot([stack[i][0], stack[i + 1][0]], [stack[i][1], stack[i + 1][1]], c='r')
        plt.plot([stack[0][0], stack[length - 1][0]], [stack[0][1], stack[length - 1][1]], c='r')
        plt.show()
        return stack

    def find_init_point(self, points):
        down_index_array = np.where(points[:, 1] == np.min(points[:, 1]))[0]
        down_points = points[down_index_array, :]
        print("down_index_array = ", down_index_array)
        left_down_index = np.argmin(down_points[:, 0])
        index = down_index_array[left_down_index]
        print("index = ", index, type(index), index.shape)
        return index

    def sort_polar_angle_cos(self, points, center_point):
        """
        按照与中心点的极角进行排序，使用的是余弦的方法
        :param points: 需要排序的点
        :param center_point: 中心点
        :return:
        """
        n = len(points)
        cos_value = []
        rank = []
        norm_list = []
        for i in range(0, n):
            point_ = points[i]
            point = [point_[0] - center_point[0], point_[1] - center_point[1]]
            rank.append(i)
            norm_value = np.sqrt(point[0] * point[0] + point[1] * point[1])
            norm_list.append(norm_value)
            if norm_value == 0:
                cos_value.append(1)
            else:
                cos_value.append(point[0] / norm_value)

        for i in range(0, n - 1):
            index = i + 1
            while index > 0:
                if cos_value[index] > cos_value[index - 1] or (
                        cos_value[index] == cos_value[index - 1] and norm_list[index] > norm_list[index - 1]):
                    temp = cos_value[index]
                    temp_rank = rank[index]
                    temp_norm = norm_list[index]
                    cos_value[index] = cos_value[index - 1]
                    rank[index] = rank[index - 1]
                    norm_list[index] = norm_list[index - 1]
                    cos_value[index - 1] = temp
                    rank[index - 1] = temp_rank
                    norm_list[index - 1] = temp_norm
                    index = index - 1
                else:
                    break
        sorted_points = []
        for i in rank:
            sorted_points.append(points[i])

        return sorted_points


if __name__ == "__main__":
    a = GrahamScan()




