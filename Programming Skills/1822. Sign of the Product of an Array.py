class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = 1
        for i in nums:
            product*= i
        def signFunc(product):
            if product>0:
                return 1
            elif product ==0:
                return 0
            else:
                return -1
        result = signFunc(product)
        return result
if __name__ == "__main__":
    sol = Solution()
    nums = [-1,-2,-3,-4,3,2,1]
    result = sol.arraySign(nums)
    print(result)