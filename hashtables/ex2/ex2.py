#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    flights = {}
    route = [None] * length # set up our route list with enough slots
    for i in range(0, length):
        curr = tickets[i]
        flights[curr.source] = curr.destination  # the starting location is the key and the destination is the value
    route[0] = flights["NONE"] # set first flight in arr to flight w/ source "NONE"
    route[1] = flights[route[0]] # found by following the i - 1 hint in read me
    if length > 2:
        for i in range(2, length):
            route[i] = flights[route[i-1]] # the `i`th location in the route can be found by checking the hash table for the `i-1`th location

    return route
