class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        distance_x = coordinates[1][0] - coordinates[0][0]
        distance_y = coordinates[1][1] - coordinates[0][1]
        for c in range(len(coordinates)-1):
            
            if coordinates[c+1][0]-coordinates[c][0]==distance_x and coordinates[c+1][1]-coordinates[c][1]==distance_y:
                continue
            else:
                return False

        return True

        
if __name__ == "__main__":
    sol = Solution()
    coordinates = [[1,2],[2,3],[3,5]]
    result = sol.checkStraightLine(coordinates) 
    
    print(result)