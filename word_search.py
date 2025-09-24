
class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"  
            
            
            found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            
            board[r][c] = temp  
            return found
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

print("Enter the board row by row (characters separated by space):")
board = [input().split() for _ in range(rows)]

word = input("Enter the word to search: ")

solution = Solution()
if solution.exist(board, word):
    print(f"The word '{word}' exists in the board!")
else:
    print(f"The word '{word}' does NOT exist in the board.")
