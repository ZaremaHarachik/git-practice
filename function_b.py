# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    sum = 0
    user_num = input("Please enter a number: ")

    while user_num != 0 or sum < 1000:
        sum += user_num
        user_num = input("Please enter the next number: ")

    return sum


if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
