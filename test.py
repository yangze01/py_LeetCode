class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1 or len(nums) == 0):
            return len(nums)
        count = 1
        for i in range(1,len(nums)):
            if(nums[i] == nums[i-1]):
                continue
            else:
                nums[count] = nums[i]
                count += 1
        # print(nums)
        return count

if __name__ == "__main__":
    # a = [1,1,2,2,5,6,7,7,9]
    # solution = Solution()
    # print(solution.removeDuplicates(a))
    # a = [1, 2, 3, 4, 5]
    # print(a.pop())
    # print(a)
    # # print(a.pop)
    # b = a.pop()
    # print(b)
    a = 3
    b = a
    b = 2
    print(a)
    print(b)
    c = [1, 2, 3]
    d = c
    d[1] = 5
    print(d)
    x = {'a': 1, 'b': 2, 'c': 3}
    x['a'] = 2123
    print(x)
