#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    # create cache
    cache = {}
    storage = [None] * length

    for i in tickets:
        if i.source == "NONE":
            storage[0] = i.destination
        cache[i.source] = i.destination

    for x in range(1, length):
        storage[x] = cache[storage[x - 1]]

    return storage


""" 
PLAN
- create a cache
- create an arr that grows with length input
- loop thru our tickets input arr
- check if our ticket source is none, bc that is our departure ticket aka number 1
-- if we found none/depart ticket then we assign our storage arr[0] to be our ticket.desination value
- udpate our cache ticket source to be the tickets destination
- loop thru range starting at 1 and end at our given length
- reconstruct our storage arr with the proper order
"""
