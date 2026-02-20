def find_max(numbers):
    if not numbers:
        return float('-inf')
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def get_first_n_items(items, n):
    return items[:n]
