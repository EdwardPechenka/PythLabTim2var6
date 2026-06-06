def get_sum(numbers):
    try:
        return sum(numbers)
    except TypeError:
        return 0