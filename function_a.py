def most_common_value(number_list):
    """ returns the most common element of the list
    """
    nums_counts = {}
    for num in number_list:
        nums_counts[num] = nums_counts.get(num, 0) + 1

    result = number_list[0]
    max_count = 0
    for num, count in nums_counts.items():
        if count > max_count:
            max_count = count
            result = num

    return result

if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
