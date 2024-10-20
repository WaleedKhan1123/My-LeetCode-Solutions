#not Complete Yet
from collections import Counter
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        counter_0 = Counter(nums)
        print(counter_0)
        movecount = 0
        for i in range(len(nums)):
            if nums[i]==0 :
                for j in range(len(nums)-1,-1,-1):
                    if nums[j]!=0:
                        nums[i],nums[j]=nums[j],nums[i]
                        print(f"nums in iteration {nums}")
                        movecount+=1
                        break
        count=len(nums)
        print(nums)
if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,0,3,12]
    result = sol.moveZeroes(nums)
    print(result)
    