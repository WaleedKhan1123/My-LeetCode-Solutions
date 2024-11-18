class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        
        newMatrix=[]
        top = 0
        bottom = len(matrix)
        
        
if __name__ == "__main__":
    sol = Solution()
    matrix = [[2,5,8],[4,0,-1]]
    result = sol.spiralOrder(matrix)
    print(result)