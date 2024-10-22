class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        same = all(x==nums[0]for x in nums)
        if same:
            return False
        for i in range(len(nums)):
            if i != (len(nums)-1):
                j=i+1
                if nums[i]<=nums[j]:
                     continue
                else:
                    return False
        return True

if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,0,0]
    result = sol.isMonotonic(nums)
    print(result)
    
    
    