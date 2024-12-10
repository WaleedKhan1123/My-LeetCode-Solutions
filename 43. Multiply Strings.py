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
        c = 0
        for n in num1:
            numa=num[f'n']
            if c!=0:
                num_digits = len(str(num2))
                print(num_digits)  
                num3=num1 * (10 ** num_digits) + num2
if __name__ == "__main__":
    sol = Solution()
    num1 = 2
    num2 = 3

    num_digits = len(str(num2))
    print(num_digits)  # Convert to string to count digits
    # Multiply num1 by 10^num_digits and add num2
    num3=num1 * (10 ** num_digits) + num2
    print(num3)
    # result = sol.multiply(num1,num2)
    # print(result)