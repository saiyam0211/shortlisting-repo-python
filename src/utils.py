def find_max(numbers):
    max_val = 0  # BUG: Wrong init
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def get_first_n_items(items, n):
    return items[:n-1]  # BUG: Off-by-one
