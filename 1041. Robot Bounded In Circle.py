class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        n = len(instructions)
        pos = (0, 0)
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        curr = 0
        for i in range(n):
            if instructions[i]=='G':
                pos = (pos[0]+directions[curr][0], pos[1]+directions[curr][1])
            elif instructions[i]=='L':
                curr = (curr + 1) % 4
            elif instructions[i]=='R':
                curr = (curr - 1) % 4
        return pos==(0, 0) or curr >0
if __name__ == "__main__":
    sol = Solution()
    instructions = "GG"
    result = sol.isRobotBounded(instructions)
    
    print(result)
    