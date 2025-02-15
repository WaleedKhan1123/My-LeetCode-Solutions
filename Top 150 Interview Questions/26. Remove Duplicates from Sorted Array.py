class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        duplicate = set()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                duplicate.add(nums[i])
        print(duplicate)
        
        
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2,2,3,4,4,4]
    val = 3
    sol.removeDuplicates(nums)
