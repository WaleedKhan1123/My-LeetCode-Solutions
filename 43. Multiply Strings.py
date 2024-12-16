#not completed yet
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num = {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9
        }
        numx=[]
        numa = 0
        numb = 0
        num3 = 0
        num4 = 0
        result=0
        c = 0
        for n in num1:
            numx.append(num[n])

        print(numx)        

        


if __name__ == "__main__":
    sol = Solution()
    num1 = "2"
    num2 = "3"
    result = sol.multiply(num1,num2)
    print(result)