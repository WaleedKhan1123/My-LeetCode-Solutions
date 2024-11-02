class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        
        a_moves = [moves[move] for move in range(0,len(moves),2)]
        b_moves = [moves[move] for move in range(1,len(moves),2)]
        win1= [[0,0],[1,1],[2,2]]
        win2= [[0,0],[1,0],[2,0]]
        win3= [[0,0],[0,1],[0,2]]
        win4= [[1,0],[1,1],[1,2]]
        win5= [[2,0],[2,1],[2,2]]
        win6= [[0,2],[1,1],[2,0]]
        win7= [[0,2],[1,2],[2,2]]
        win8= [[0,1],[1,1],[2,1]]
        if all(move in a_moves for move in win1 ) or all(move in a_moves for move in win2 ) or all(move in a_moves for move in win3 ) or all(move in a_moves for move in win4 ) or all(move in a_moves for move in win5 ) or all(move in a_moves for move in win6 ) or all(move in a_moves for move in win7 ) or all(move in a_moves for move in win8 ):
         return "A"
        elif all(move in b_moves for move in win1 ) or all(move in b_moves for move in win2 ) or all(move in b_moves for move in win3 ) or all(move in b_moves for move in win4 ) or all(move in b_moves for move in win5 ) or all(move in b_moves for move in win6 ) or all(move in b_moves for move in win7 ) or all(move in b_moves for move in win8 ):
            return "B"
        else:
            if len(moves)==9:
                return "Draw"
            return "Pending"
        
        
if __name__ == "__main__":
    sol = Solution()
    moves = [[0,0],[2,2],[1,0],[2,0],[0,1],[1,2],[1,1],[0,2]]
    result = sol.tictactoe(moves) 
    
    print(result)
    
    