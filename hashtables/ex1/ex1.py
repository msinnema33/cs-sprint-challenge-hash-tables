def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight = {}
    dupe_check = False # in order to pass test #2
    dupes = {} # we need to account for duplicat weights ie: [10,10] This is an edge case!!!!!
    #loop through weights and store them in the dict
    for i in range(0, length):
        current = weights[i]
        weight[current] = i #set the value to the index
        target = limit - current # we subtract the current value from the limit to find which package combines to equal weight limit
        if target in weight:
            if current > target or current < target:
                return (i, weight[target])
            elif target == current: # if it finds a dupe
                if dupe_check is False:
                    dupe_check = True
                    dupes[current] = i
                elif dupe_check is True:
                    return (i, dupes[current])

    return None
