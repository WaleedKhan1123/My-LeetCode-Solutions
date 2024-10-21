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
        digits = [int(digit) for digit in str(num)]
        return digits
if __name__ == "__main__":
    sol = Solution()
    digits = [9,9,9]
    result = sol.plusOne(digits)
    print(result)        