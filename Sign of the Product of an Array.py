class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            print(nums[i]*nums[(i+1)])
if __name__ == "__main__":
    sol = Solution()
    nums = [-1,-2,-3,-4,3,2,1]
    result = sol.arraySign(nums)
    print(result)