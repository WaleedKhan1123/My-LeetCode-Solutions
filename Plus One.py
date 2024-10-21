class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=""
        for i in digits:
            num+=str(i)
        print(num[1])
        
        return digits
if __name__ == "__main__":
    sol = Solution()
    digits = [1,2,3]
    result = sol.plusOne(digits)
    print(result)        