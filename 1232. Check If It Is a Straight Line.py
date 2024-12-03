class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        distance = coordinates[1][0] - coordinates[0][0]

        print(distance)        
if __name__ == "__main__":
    sol = Solution()
    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    result = sol.checkStraightLine(coordinates) 
    
    print(result)