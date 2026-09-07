class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        new_grid = []
        cols, rows = len(boxGrid), len(boxGrid[0])

        for i in range(rows):
            new_grid.append([])
            for j in range(cols):
                new_grid[i].append(boxGrid[cols-j-1][i])
        
        #handle gravity in groups
        #1. determine how many rocks are in each group that need to fall
        groups = []
        for i in range(cols):
            groups.append([])
            curr_count = 0
            for j in range(rows-1, -1, -1):
                if new_grid[j][i] == "#":
                    curr_count += 1
                if new_grid[j][i] == "*" or j == 0:
                    groups[-1].append(curr_count)
                    curr_count = 0
        
        for i in range(cols):
            curr_group = 0
            for j in range(rows-1, -1, -1):
                if new_grid[j][i] != "*":
                    if groups[i][curr_group] > 0:
                        new_grid[j][i] = "#"
                        groups[i][curr_group] -= 1
                    else:
                        new_grid[j][i] = "."
                else:
                    curr_group += 1
        
        return new_grid

"""
###
###
##*
#*.
#.*
#..
"""
        

