class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<=1:
            return False
        if all(x==arr[0] for x in arr):
            return True
        arr = sorted(arr)
        print(arr)
        difference = arr[1]-arr[0]
        if difference==0:
            return False
        check=0
        for i in range(len(arr)-1):
            check = arr[i]+difference
            print(check)
            if(check != arr[i+1]):
                return False
        return True
if __name__ == "__main__":
    sol = Solution()
    arr = [1,10,10,10,19]
    result = sol.canMakeArithmeticProgression(arr)
    print(result)        