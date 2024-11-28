def compute_prefix_sum(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    # Initialize prefix sum for sum of non-negative values and count of non-negative values
    sum_prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    count_prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            value = matrix[i-1][j-1]
            is_non_neg = 1 if value >= 0 else 0
            value = max(0, value)  # Ignore negative values, treat them as 0
            
            # Build prefix sums
            sum_prefix[i][j] = sum_prefix[i-1][j] + sum_prefix[i][j-1] - sum_prefix[i-1][j-1] + value
            count_prefix[i][j] = count_prefix[i-1][j] + count_prefix[i][j-1] - count_prefix[i-1][j-1] + is_non_neg
    
    return sum_prefix, count_prefix

def get_sum_and_count(sum_prefix, count_prefix, r1, c1, r2, c2):
    total_sum = sum_prefix[r2][c2] - sum_prefix[r1-1][c2] - sum_prefix[r2][c1-1] + sum_prefix[r1-1][c1-1]
    total_count = count_prefix[r2][c2] - count_prefix[r1-1][c2] - count_prefix[r2][c1-1] + count_prefix[r1-1][c1-1]
    return total_sum, total_count

def calculate_average(sum_prefix, count_prefix, r1, c1, r2, c2):
    total_sum, total_count = get_sum_and_count(sum_prefix, count_prefix, r1, c1, r2, c2)
    if total_count == 0:
        return float('-inf')  # Invalid partition
    return total_sum // total_count

def minimize_difference(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    # Step 1: Compute prefix sums
    sum_prefix, count_prefix = compute_prefix_sum(matrix)
    
    min_difference = float('inf')
    best_row, best_col = -1, -1
    
    # Step 2: Try all possible partition points
    for resRow in range(1, rows):
        for resCol in range(1, cols):
            # Calculate average for each partition
            top_left_avg = calculate_average(sum_prefix, count_prefix, 1, 1, resRow, resCol)
            top_right_avg = calculate_average(sum_prefix, count_prefix, 1, resCol + 1, resRow, cols)
            bottom_left_avg = calculate_average(sum_prefix, count_prefix, resRow + 1, 1, rows, resCol)
            bottom_right_avg = calculate_average(sum_prefix, count_prefix, resRow + 1, resCol + 1, rows, cols)
            
            # Get the valid averages
            averages = [top_left_avg, top_right_avg, bottom_left_avg, bottom_right_avg]
            max_avg = max(averages)
            min_avg = min(averages)
            
            # Ensure all submatrices have at least one non-negative value
            if min_avg != float('-inf'):
                difference = max_avg - min_avg
                if difference < min_difference:
                    min_difference = difference
                    best_row, best_col = resRow, resCol
    
    return best_row - 1, best_col - 1  # Return 0-based indices

# Example Usage
matrix = [
    [1, -2, 3],
    [-1, 5, 6],
    [7, -8, 9]
]

matrix = [
    [6, 1, 3, 4],
    [-1, 9, -3, 1],
    [7, -8, 5, 2],
    [0, 5, -1, 2]
]

result = minimize_difference(matrix)
print(result)  # Output the optimal row and column for partitioning
