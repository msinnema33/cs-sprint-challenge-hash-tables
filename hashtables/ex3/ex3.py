def intersection(arrays):
    """
    YOUR CODE HERE
    """
    store = dict()
    res = []
    for index, arr in enumerate(arrays): # list all of the elements of a set
        for v in arr:
            if store.get(v) is not None and index > 0: #.get returns value from storage
                store[v] += 1 # we either add on to an existing value indicating it's found in more than one arr
            elif store.get(v) is None and index == 0:
                store[v] = 1 #or we start a new spot for the first arr's value
            else:
                continue # if a new num in a following arr that wasnt seen in previous arr, skip it as it cannot be in common
    for values in store:
        if store[values] == len(arrays):
            res.append(values) # if val is present in all subarrays, add to result list
    return res


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
