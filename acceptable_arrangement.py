

if __name__ == '__main__':
    r, c = map(int, input().split())
    nums = []
    m = {}
    for _ in range(r):
        temp = input().split()
        for s in temp:
            m[int(s)] = ()
            nums.append(int(s))
    
    for row in range(r):
        col = 1
        temp = input().split()
        for s in temp:
            m[int(s)] = (row+1, col)
            col += 1
    
    if r == 1:
        print(0)
        exit()
    
    arr = [[0] * (c+2) for _ in range(r+1)]
    
    i = 0
    
    for row in range(1, r+1):
        for col in range(1, c+2):
            if col == c+1:
                arr[row][col] = r * c + 1
            else:
                arr[row][col] = nums[i]
                i += 1
    swaps = 0
    steps = []
    for row in range(1, r+1):
        for col in range(1, c+1):     
            while True:
                num1 = arr[row][col]
                newRow, newCol = m[num1]
                if row == newRow and col == newCol:
                    break
                num2 = arr[newRow][newCol]
                if arr[newRow][newCol-1] < num1 < arr[newRow][newCol+1] and arr[row][col-1] < num2 < arr[row][col+1]:
                    arr[row][col] = num2
                    arr[newRow][newCol] = num1
                    swaps += 1
                    steps.append('%s %s %s %s' % (row, col, newRow, newCol))
                else:
                    break
    
    print(arr)
    
    print(swaps)            
    for s in steps:
        print(s)
                    
                
            
        
    