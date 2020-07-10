def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # dict to hold all nums in a
    store = {}
    # arr to return matches in absolute value(result)
    res = []
    for num in a:
        # if the num has a corresponding number in dict
        if store.get(abs(num)): # .get method returns the value for the given key
            res.append(abs(num)) # if so add to results list
        else:
            # if no val is found add num (the value) to the store
            store[abs(num)] = num

    return res


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
