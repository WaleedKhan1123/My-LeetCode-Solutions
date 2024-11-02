class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        Directions = {
            
            "North":0,
            "South":0,
            "West":0,
            "East":0
        }
        
        
if __name__ == "__main__":
    sol = Solution()
    instructions = "GGLLGG"
    result = sol.isRobotBounded(instructions)
    
    print(result)
    