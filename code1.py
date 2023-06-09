grid=[
    [7,4,3,2,1,5,6,7,5],
    [6,5,4,3,7,6,5,9,8],
    [2,7,4,6,5,9,7,8,5],
    [9,7,8,6,5,4,6,3,2],
    [8,5,4,7,5,6,8,6,1],
    [7,4,5,6,2,3,4,6,7],
    [8,5,6,2,3,5,4,1,2],
    [2,3,4,1,5,3,6,7,8],
    [6,4,3,5,2,6,8,9,7],
]

def check_row(grid,row_no,element):
 for column in range(9):
     print(grid[row_no][column])
     if grid[row_no][column]==element:
        return True
 return False
    
print(check_row(grid,0,8))

def check_column(grid,column_no,element):
 for row in range(9):
     print(grid[row][column_no])
     if grid[row][column_no]==element:
        return True
 return False
    
print(check_column(grid,0,8))

def check_diag(grid):
   for i in range(9):
      print(grid[i][i])

check_diag(grid)
