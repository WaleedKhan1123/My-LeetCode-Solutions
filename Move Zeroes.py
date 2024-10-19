#not Complete Yet
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        count=len(nums)
        print(nums[-1:])
if __name__ == "__main__":
    sol = Solution()
    nums = [0]
    result = sol.moveZeroes(nums)
    print(result)
    