class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row , column = [],[]
        for r in range(len(matrix)):
            
            for c in range(len(matrix[r])):
                 
                 if matrix[r][c] == 0:
                    row.append(r)
                    column.append(c)
        for i,j in zip(row,column):

            for r in range(len(matrix)):
                matrix[r][j]=0

            for c in range(len(matrix[0])):
                    matrix[i][c] = 0
        
if __name__ == "__main__":
    sol = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol.setZeroes(matrix)
    print(matrix)       