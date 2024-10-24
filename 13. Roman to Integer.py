# not completed yet
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = ['I','V','X','L','C','D','M']
        numbers= ['1','5','10','50','100','500','1000']
        numlist = []
        for i in range(len(s)):
            for j in range(len(romans)):
               if s[i] == romans[j]:
                   numlist.append(numbers[j]) 
        num=0
        for i in numlist:
            num+=int(i)
        return num
if __name__ == "__main__":
    sol = Solution()
    s = "XXVII"
    result = sol.romanToInt(s)
    print(result)