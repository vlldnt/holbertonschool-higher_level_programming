def max_integer(my_list=[]):
    sorted_list = sorted(my_list, key=int, reverse=True)
    if sorted_list:
        return sorted_list[0]
    return None
