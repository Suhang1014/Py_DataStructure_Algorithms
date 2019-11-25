# _*_ coding:utf-8 _*_
import numpy as np
import random
import re
import matplotlib.pyplot as plt


def load_dataset():
    dataset = np.loadtxt('dataset.csv')
    return dataset


def show_fig():
    dataset = load_dataset()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataset[:, 0], dataset[:, 1])
    plt.show()


def cal_distance(vec1, vec2):
    return np.sqrt(np.sum(np.square(vec1 - vec2)))


def init_centroids(dataset, k):
    # 随机选取k个数据作为初始质心
    dataset = list(dataset)
    return random.sample(dataset, k)


def min_distance(dataset, centroid_list):
    # 对每个属于dataSet的item， 计算item与centroidList中k个质心的距离，找出距离最小的，并将item加入相应的簇类中
    cluster_dict = dict()
    k = len(centroid_list)
    for item in dataset:
        vec1 = item
        flag = -1
        min_dis = float('inf')
        for i in range(k):
            vec2 = centroid_list[i]
            distance = cal_distance(vec1, vec2)
            if distance < min_dis:
                min_dis = distance
                flag = i # 循环结束时，flag保存与当前item最近的簇标记
        if flag not in cluster_dict.keys():
            cluster_dict.setdefault(flag, [])
        cluster_dict[flag].append(item) # 加入相应的类别中
    return cluster_dict


def get_centroid(cluster_dict):
    # 重新计算k个质心
    centroid_list = []
    for key in cluster_dict.keys():
        centroid = np.mean(cluster_dict[key], axis=0)
        centroid_list.append(centroid)
    # 得到新的质心
    return centroid_list


def get_var(centroid_list, cluster_dict):
    # 计算各蔟集合间的均方误差
    # 将蔟类中各个向量与质心的距离累加求和
    sum = 0.0
    for key in cluster_dict.keys():
        vec1 = centroid_list[key]
        distance = 0.0
        for item in cluster_dict[key]:
            vec2 = item
            distance += cal_distance(vec1, vec2)
        sum += distance
    return sum


def show_cluster(centroid_list, cluster_dict):
    # 展示聚类结果
    colorMark = ['or', 'ob', 'og', 'ok', 'oy', 'ow'] #不同簇类标记，o表示圆形，另一个表示颜色
    centroidMark = ['dr', 'db', 'dg', 'dk', 'dy', 'dw']

    for key in cluster_dict.keys():
        plt.plot(centroid_list[key][0], centroid_list[key][1], centroidMark[key], markersize=12) #质心点
        for item in cluster_dict[key]:
            plt.plot(item[0], item[1], colorMark[key])
    plt.show()


def test_k_means():
    dataset = load_dataset()
    centroid_list = init_centroids(dataset, 4)
    cluster_dict = min_distance(dataset, centroid_list)
    # # getCentroids(clusterDict)
    # showCluster(centroidList, clusterDict)
    new_var = get_var(centroid_list, cluster_dict)
    old_var = 1  # 当两次聚类的误差小于某个值是，说明质心基本确定。

    times = 2
    while abs(new_var - old_var) >= 0.00001:
        centroid_list = get_centroid(cluster_dict)
        cluster_dict = min_distance(dataset, centroid_list)
        old_var = new_var
        new_var = get_var(centroid_list, cluster_dict)
        times += 1
        show_cluster(centroid_list, cluster_dict)


if __name__ == '__main__':
    # show_fig()
    test_k_means()







