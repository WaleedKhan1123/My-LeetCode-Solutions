class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        same = all(x==nums[0]for x in nums)
        if same:
            return True
        incdec = any(num>nums[0] for num in nums[1:])
        for i in range(len(nums)):
            if i != (len(nums)-1):
              j=i+1
              if incdec:
                if nums[i]<=nums[j]:
                     continue
                else:
                    return False
              else:
                  if nums[i]>=nums[j]:
                     continue
                  else:
                    return False
        return True

if __name__ == "__main__":
    sol = Solution()
    nums = [4,3,2,1]
    result = sol.isMonotonic(nums)
    print(result)
    
    
    