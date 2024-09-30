def find_max_min(arr, low, high):
    if low == high:
        return arr[low], arr[low]
        if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
        mid = (low + high) // 2
        left_min, left_max = find_max_min(arr, low, mid)
    right_min, right_max = find_max_min(arr, mid + 1, high)
        overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)
    
    return overall_min, overall_max
arr = [3, 5, 1, 8, 2, 7, 6, 4]
min_val, max_val = find_max_min(arr, 0, len(arr) - 1)
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")
