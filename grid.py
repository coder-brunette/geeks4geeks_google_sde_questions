from collections import deque

# class Solution (object):
#     def shortestPath(self, grid, k):
#     # type grid: List[List[int]] 
#     # type k: int 
#     # rtype: int
#         start = [0,0,k,0] # start, end, num_available, num_steps
#         if len(grid) == 1 and len(grid[0]) == 1:
#             return 0
#         q = deque()
#         q.append(start)
#         directions = ((-1,0),(1,0),(0,1),(0,-1)) # top, down, right, left
#         visited = set((0,0,k))
#         while q:
#             current_row, current_col, num_available, curr_steps = q.popleft()
#             for row_dir, col_dir in directions:
#                 next_row, next_col = current_row + row_dir, current_col + col_dir
#                 if next_row == len(grid) - 1 and next_col == len(grid[0]) -1: # exit condition
#                     return curr_steps + 1
#                 if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]): # checking inbounds
#                     if (next_row, next_col, num_available) in visited: # already visited
#                         continue
#                     if grid[next_row][next_col] == 0: # no obstacle
#                         visited.add((next_row,next_col,num_available))
#                         q.append([next_row, next_col, num_available, curr_steps+1])
#                     else: # there is an obstacle
#                         if num_available > 0 : # at least one removal left
#                             visited.add((next_row,next_col,num_available))
#                             q.append([next_row,next_col,num_available-1,curr_steps+1])

#         return -1
    
def shortestPath(grid, k):
    start = [0,0,k,0] 
    if len(grid) == 1 and len(grid[0]) == 1:
        return 0
    q = deque()
    q.append(start)
    directions = ((1,0),(-1,0),(0,-1),(0,1))
    visited = set((0,0,k))
    while q:
        current_row, current_col, num_available, current_steps = q.popleft()
        for row_dir, col_dir in directions:
            next_row, next_col = current_row + row_dir, current_col + col_dir
            if next_row == len(grid) -1 and next_col == len(grid[0]) - 1:
                return current_steps + 1
            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                if (next_row,next_col,num_available) in visited:
                    continue
                if grid[next_row][next_col] == 0:
                    visited.add((next_row,next_col,num_available))
                    q.append([next_row,next_col,num_available,current_steps+1])
                else:
                    if num_available > 0:
                        visited.add((next_row,next_col,num_available))
                        q.append([next_row,next_col,num_available-1,current_steps+1])
    return -1



print(shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]],1))















