class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []
        
        for m in matrix:
            
            for i in m:
                spiral.append(i)
        print(spiral)
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    result = sol.spiralOrder(matrix)
    print(result)