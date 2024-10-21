class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=""
        for i in digits:
            num+=str(i)
        num = int(num)
        num+=1
        print(num)
        return digits
if __name__ == "__main__":
    sol = Solution()
    digits = [1,2,3]
    result = sol.plusOne(digits)
    print(result)        