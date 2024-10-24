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
                   if (s[i] =='V' and s[i-1]=='I') or (s[i] =='X' and s[i-1]=='I') :
                       numlist.append(int(numbers[j])-(int(numbers[0])*2))
                   elif (s[i] =='L' and s[i-1]=='X') or (s[i] =='C' and s[i-1]=='X') :
                       numlist.append(int(numbers[j])-(int(numbers[2])*2))
                   elif (s[i] =='D' and s[i-1]=='C') or (s[i] =='M' and s[i-1]=='C')  :
                       numlist.append(int(numbers[j])-(int(numbers[4])*2))
                   else:
                       numlist.append(int(numbers[j])) 
        num=0
        for i in range(len(numlist)):
                num+=numlist[i]
        return num
if __name__ == "__main__":
    sol = Solution()
    s = "MCMXCIV"
    result = sol.romanToInt(s)
    print(result)