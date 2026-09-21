def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    max_val = numbers[0]
    for num in numbers:
        max_val = max(max_val, num)
    return max_val
# comment 

# Experiment

if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
