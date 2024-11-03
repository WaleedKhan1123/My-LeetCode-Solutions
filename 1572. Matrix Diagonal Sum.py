class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum=0
        second_i=0
        for i in range(len(mat[0])):
            sum+=mat[i][i]
        print(sum)
        for i in range(len(mat[0]) - 1, -1, -1):
            print(i)
            sum+=mat[second_i][i]
            second_i+=1
            print(second_i)
        
        print(sum)
        
if __name__ == "__main__":
    sol = Solution()
    
    mat = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    
    result = sol.diagonalSum(mat)
    
    print(result)