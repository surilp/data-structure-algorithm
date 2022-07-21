
def kadane_algo(array):
    current_sum = -float('inf')
    max_sum = -float('inf')
    for num in array:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadane_algo(array))