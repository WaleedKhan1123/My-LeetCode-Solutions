#not done yet
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        print(nums)
        print(val)
        count = nums.count(val)
        print(count)
        indexCount =  [i for i,num in enumerate(nums) if num == val]
        print(indexCount)
        i = 0
        while len(indexCount)>0:
             
             nums.pop(indexCount[i])
             indexCount = [i for i,num in enumerate(nums) if num == val]
             i-=1
        print(nums)
        
if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,2,3]
    val = 3
    sol.removeElement(nums,val)
