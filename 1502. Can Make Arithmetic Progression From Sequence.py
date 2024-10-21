class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<=1:
            return False
        arr = sorted(arr)
        difference = arr[1]-arr[0]
        print(difference)
        for i in arr:
            difference+=i
            print(i)
            if(difference not in arr):
                return False
        return True
if __name__ == "__main__":
    sol = Solution()
    arr = [0,1,2]
    result = sol.canMakeArithmeticProgression(arr)
    print(result)        