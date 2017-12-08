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

# 递归方法实现归并排序
def merge_sort(lists):
    # 认为长度不大于1的数列是有序的
    if len(lists) <= 1:
        return lists
    # 二分列表
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    # 最后一次合并
    return merge(left, right)

# 合并
def merge(left, right):
    l,r=0,0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] <right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
        # print(l,r)
    result += left[l:]
    result += right[r:]
    return result

# 迭代方法实现归并排序
def merge_sort2(lists):
    length = len(lists)
    step = 1
    # 步长为1, 2, 4, 8, ..., 一直合并下去
    while step <= length:
        offset = step << 1
        for index in range(0, length, offset):
            merge2(lists, index, min(index+step, length-1), min(index+offset-1, length-1))
        step = offset

def merge2(lists, head1, head2, tail2):
    # 合并两个排好序的区间：[head1, tail1]与[head2, tail2]
    tail1 = head2 - 1
    start = head1
    index = 0
    tmp = [0] * (tail2-head1+1)
    while head1 <= tail1 or head2 <= tail2:
        if head1 > tail1:
            tmp[index] = lists[head2]
        elif head2 > tail2:
            tmp[index] = lists[head1]
        else:
            if lists[head1] <= lists[head2]:
                tmp[index] = lists[head1]
            else:
                tmp[index] = lists[head2]

        if head1 <= tail1 and tmp[index] == lists[head1]:
            head1 += 1
        else:
            head2 += 1
        index += 1

    for i in range(start, tail2 + 1):
        lists[i] = tmp[i-start]

# 快速排序 递归
def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right

    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists
# 快速排序
def quick_sort2(lists):
    less = []
    pivotList = []
    more = []
    # 递归出口
    if len(lists) <= 1:
        return lists
    else:
        # 第一个值为基准
        pivot = lists[0]
        for i in lists:
            # 将比base小的值放到less里面
            if i < pivot:
                less.append(i)
            # 将比base大的值放到More里面
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quick_sort2(less)
        more = quick_sort2(more)
        return less + pivotList + more
def adjust_heap(lists, i, size):
    # print(1)
    lchild = 2 * i + 1 # i的左孩子节点序号
    rchild = 2 * i + 2 # i的右孩子节点序号
    max = i
    if i <= size/2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[i], lists[max] = lists[max], lists[i]
            adjust_heap(lists, max, size) # 避免调整之后以max为父节点的子树不是堆


def build_heap(lists, size):

    for i in range(0, (int(size/2)))[::-1]:
        adjust_heap(lists, i, size)

def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    return lists


if __name__ == "__main__":
    # print(1)
    lists = [7, 13, 3, 1, 5, 10, 2, 20]
    print("bubble_sort")
    print(bubble_sort(lists))
    lists = [7, 13, 3, 1, 5, 10, 2, 20]
    print("bubble_sort2")
    print(bubble_sort_flag(lists))
    lists = [7, 13, 3, 1, 5, 10, 2, 20]
    print("selection sort")
    print(bubble_sort_flag(lists))
    lists = [7, 13, 3, 1, 5, 10, 2, 20]
    print("insert sort")
    print(insert_sort2(lists))
    lists = [7, 13, 3, 1, 5, 10, 2, 20]
    print("shell sort")
    print(shell_sort(lists))
    lists = [7, 13, 3, 1, 5, 10, 2, 20]
    print("merge sort")
    print(merge_sort(lists))
    lists = [7, 13, 3, 1, 5, 10, 2, 20]
    print("merge sort2")
    merge_sort2(lists)
    print(lists)
    lists = [7, 13, 3, 1, 5, 10, 2, 20]
    print("quick sort")
    print(quick_sort(lists, 0, len(lists)-1))
    lists = [7, 13, 3, 1, 5, 10, 2, 20]
    print("heap sort")
    print(heap_sort(lists))

