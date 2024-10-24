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
                   if s[i] =='V' and s[i-1]=='I'  :
                       numlist.append(int(numbers[j])-(int(numbers[j-1])*2))
                   elif s[i] =='X' and s[i-1]=='I'  :
                       numlist.append(int(numbers[j])-(int(numbers[j-1])*2))
                   elif s[i] =='L' and s[i-1]=='X'  :
                       numlist.append(int(numbers[j])-(int(numbers[j-1])*2))
                   elif s[i] =='V' and s[i-1]=='L'  :
                       numlist.append(int(numbers[j])-(int(numbers[j-1])*2))
                   elif s[i] =='C' and s[i-1]=='D'  :
                       numlist.append(int(numbers[j])-(int(numbers[j-1])*2))
                   elif s[i] =='D' and s[i-1]=='M'  :
                       numlist.append(int(numbers[j])-(int(numbers[j-1])*2))
                   else:
                       numlist.append(int(numbers[j])) 
        num=0
        for i in range(len(numlist)):
                num+=numlist[i]
        return num
if __name__ == "__main__":
    sol = Solution()
    s = "IX"
    result = sol.romanToInt(s)
    print(result)