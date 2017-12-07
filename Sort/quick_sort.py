#coding=utf8
import random
class Stack(object):
    def __init__(self, size):
        """
            初始化得到一个空栈
        :param size:
        """
        self.size = size
        self.stack = []

    def __str__(self):
        """
        返回栈内容
        :return:
        """
        return str(self.stack)

    def getSize(self):
        """
        获取栈当前的大小
        :return:
        """
        return len(self.stack)

    def push(self, ele):
        """
        将一个元素压入栈
        :param ele:
        :return:
        """
        if self.isFull():
            raise Exception("Empty Stack!!!")
        self.stack.append(ele)

    def top(self):
        """
        返回栈顶元素
        :return:
        """
        if self.isEmpty():
            raise Exception("Empty Stack!!!")
        return self.stack[-1]

    def pop(self):
        """
        弹出栈顶元素
        :return:
        """
        if self.isEmpty():
            raise Exception("Empty Stack!!!")
        return self.stack.pop()

    def isEmpty(self):
        """
        判断栈是否为空
        :return:
        """
        if len(self.stack) == 0:
            return True
        return False

    def isFull(self):
        """
        判断当前栈是否已满
        :return:
        """
        if len(self.stack) == self.size:
            return True
        return False

def partition(nums, left, right):
    """
        划分函数，返回划分下标
    :param nums:
    :param start:
    :param end:
    :return:
    """
    key = nums[left]
    low = left
    high = right
    while low < high:
        while low < high and nums[high] >= key:
            high -= 1
        nums[low] = nums[high]
        while low < high and nums[low] <= key:
            low += 1
        nums[high] = nums[low]
        nums[low] = key
    return low

def quickSort(lists, left, right):
    """
    递归解法
    :param lists:
    :param left:
    :param right:
    :return:
    """
    if lists == [] or left < 0 or right <= 0 or left > right:
        return
    k = partition(lists, left, right)
    if k > left:
        quickSort(lists, left, k-1)
    if k < right:
        quickSort(lists, k+1, right)


def random_nums_generator(max_value = 100, total_nums = 20):
    ''''
        随机数列表生成器
        一些常用函数：
        random随机数生成
        random.random()用于生成一个0到1之间的随机数:0 <= n < 1.0；
        random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。min(a,b) <= n <= max(a,b)；
        randdom.randint(a, b), 用于生成一个指定范围内的整数，其中a是下限，b是上限： a<= n <= b；
        random.randrange(start, stop, step), 从指定范围内，按指定基数递增的集合获取一个随机数；
        random.choice(sequence), 从序列中获取一个随机元素；
        random.shuffle(x), 用于将一个列表中的元素打乱；
        random.sample(sequence, k), 从指定序列中随机获取指定长度的片断；
    '''
    num_list = []
    for i in range(total_nums):
        num_list.append(random.randint(0, max_value))
    return num_list

if __name__ == "__main__":
    a = random_nums_generator()
    print(a)
    quickSort(a, 0, len(a)-1)
    print(a)







