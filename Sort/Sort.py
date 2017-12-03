#coding=utf8
import sys
"""
算法复习开始: 八大排序算法
"""
def bubble_sort(list):
    """
        冒泡排序
    :param list:
    :return:
    """
    length = len(list)
    # 第一级遍历
    for index in range(length):
        # 第二级遍历
        for j in range(1, length - index):
            if list[j-1] > list[j]:
                # 交换两者数据
                list[j-1], list[j] = list[j], list[j-1]
    return list

def bubble_sort_flag(list):
    """
        改进冒泡排序，如果已经是顺序的，则不用进行排序，直接返回结果
    :param list:
    :return:
    """
    length = len(list)
    for index in range(length):
        # 标志位
        flag = True
        for j in range(1, length - index):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
                flag = False
        if flag:
            return list
    return list

def selection_sort(list):
    """
        选择排序，每次将序列中最小或者最大的元素找出来，
        然后放在序列的起始位置
    :param list:
    :return:
    """
    n = len(list)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if list[j] < list[min_index]:
                min_index = j
                list[min_index], list[i] = list[i], list[min_index]
    return list

def insert_sort(list):
    """
        插入排序，通过构建有序序列，对于未排序的数据，
        在已排序序列中从后向前扫描，找到相应位置并插入。
        步骤
        1. 从第一个元素开始，该元素可以认为已经被排序
        2. 取出下一个元素，在已经排序的序列中从后向前扫描
        3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
        4. 重复步骤3， 直到找到已排序的元素小于或者等于新元素的位置
        5. 将新元素插入到该位置后
        6. 重复步骤2-5
    :param list:
    :return:
    """
    n = len(list)
    for i in range(1, n):
        # 后一个元素跟前一个元素比较
        # 如果比前一个小
        if list[i] < list[i - 1]:
            # 将这个数取出
            temp = list[i]
            # 保存下标
            index = i
            # 从后往前一次比较每个元素
            for j in range(i - 1, -1, -1):
                # 和比取出元素大的元素交换
                if list[j] > temp:
                    list[j + 1] = list[j]
                    index = j
                else:
                    break
            # 插入元素
            list[index] = temp
    return list

def insert_sort2(lists):
    """
        插入排序
    :param lists:
    :return:
    """
    # 插入排序
    count = len(lists)
    # 每次遍历已经排好序的部分，生成结果。
    for i in range(1, count):
        # 记录当前元素
        key = lists[i]
        j = i - 1
        # 从已经排好序的元素开始，遍历当前元素应该插入到哪一个
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

# def insert_sort3(lists):
#     count = len(lists)
#     for i in range(1, count):
#         # 记录当前元素
#         key = lists[i]
#         j = i - 1
#         while j >= 0:
#             if lists[j] > key:
#                 lists[j+1] = lists[j]
#                 lists[j] = key
#             j -= 1
#     return lists



def shell_sort(lists):
    """
        希尔排序，每次以一定的步长（跳过等距的数）进行排序，直至步长为1.
    :param list:
    :return:
    """
    n = len(lists)
    # 初始步长
    gap = round(n/2)
    while gap > 0:
        for i in range(gap, n):
            # 每个步长进行插入排序
            temp = lists[i]
            j = i
            # 插入排序
            # while j >= gap and list[j - gap] > temp:
            #     list[j] = list[j - gap]
            while j >= gap and lists[j - gap] > temp:
                lists[j] = lists[j - gap]
                j -= gap
            lists[j] = temp
        # 得到新的步长
        gap = round(gap / 2)
    return lists

# def shell_sort(lists):
#     """
#     希尔排序, 每次以一定的步长（跳过等距的数）进行排序，直到步长为1
#     :param lists:
#     :return:
#     """
#     n = len(lists)
#     # 初始步长
#     gap = round(n/2)
#     while gap > 0:
#         for i in range(gap, n):
#             # 每个步长进行插入排序
#             temp = lists[i]
#             j = i
#             # 插入排序
#             while j >= gap and lists[j - gap] > temp:
#                 lists[j] = lists[j - gap]
#                 j -= gap
#             lists[j] = temp
#         # 得到新的步长
#         gap = round(gap/2)
#     return lists





if __name__ == "__main__":
    # print(1)
    lists = [7, 13, 3, 1, 5, 10, 2, 20]
    print("bubble_sort")
    print(bubble_sort(lists))
    print("bubble_sort2")
    print(bubble_sort_flag(lists))
    print("selection sort")
    print(bubble_sort_flag(lists))
    print("insert sort")
    print(insert_sort2(lists))


