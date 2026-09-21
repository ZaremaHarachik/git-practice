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
    sum += int(user_num)

    while int(user_num) != 0 and sum < 1000:
        sum += int(user_num)
        user_num = input("Please enter the next number: ")

    return sum


if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
