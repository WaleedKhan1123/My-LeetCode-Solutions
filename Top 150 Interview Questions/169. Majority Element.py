class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)/2
        print(n)
        counter = 0
        current_frequent = None
        for i in nums:
            if i != current_frequent:
                print(i)
                for j in nums:
                    if j == i:
                       counter+=1
                    if counter>n:
                        current_frequent = j
            counter=0
        return current_frequent
            
             

                
    
        
if __name__ == "__main__":
    sol = Solution()
    nums = [3,3,4]
    result = sol.majorityElement(nums)
    print(result)