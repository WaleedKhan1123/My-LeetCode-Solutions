#not completed yet 
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for r in matrix:
            
            for c in r:
                print(c)
        
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    result = sol.setZeroes(matrix)
    print(result)       