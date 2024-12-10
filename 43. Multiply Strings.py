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
        
        numa = 0
        numb = 0
        num3 =0
        c = 0
        if len(num1)==1:
            numa=num[f'{num1}']
        else:

            for n in num1:
                numa=num[f'{n}']
                if c!=0:
                    num_digits = len(str(numa))
                    print(num_digits)  
                    num3=num1 * (10 ** num_digits) + num2
                c+=1
        if len(num2)==1:
            numb=num[f'{num2}']
        else:

            for n in num1:
                numa=num[f'{n}']
                if c!=0:
                    num_digits = len(str(numa))
                    print(num_digits)  
                    num3=num1 * (10 ** num_digits) + num2
                c+=1
        print(numa*numb)
if __name__ == "__main__":
    sol = Solution()
    num1 = "2"
    num2 = "3"
    result = sol.multiply(num1,num2)
    print(result)