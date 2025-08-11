class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate

    
        
if __name__ == "__main__":
    sol = Solution()
    nums =[2,2]
    result = sol.majorityElement(nums)
    print(result)