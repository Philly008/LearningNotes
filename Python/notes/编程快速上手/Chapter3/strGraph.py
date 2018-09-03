# -*- coding:utf-8 -*-
import copy

grid = [ ['.', '.', '.', '.', '.', '.'],
         ['.', '0', '0', '.', '.', '.'],
         ['0', '0', '0', '0', '.', '.'],
         ['0', '0', '0', '0', '0', '.'],
         ['.', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '.'],
         ['0', '0', '0', '0', '.', '.'],
         ['.', '0', '0', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.'],
         ]
c = []
c = copy.deepcopy(grid)
gridLen = len(grid)
cyctime = len(grid[0])
i = 0
j = 0
for j in range(cyctime):
    if j < cyctime:
        for i in range(gridLen):
            if i < gridLen:
                print(c[i][j], end = ' ')
                i = i + 1
    print('\n')
    j = j + 1