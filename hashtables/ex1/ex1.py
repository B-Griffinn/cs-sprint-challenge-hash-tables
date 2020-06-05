# create a cache
cache = {}


def get_indices_of_item_weights(weights, length, limit):

    # loop through our weights arr but stop at length
    for i in range(0, len(weights)):
        # store each weight as the key
        # print(weights[i])
        if weights[i] not in cache:
            # store each weight index as the value
            cache[i] = weights[i]
            # print("CACHE", cache[i])

    # loop thru cache
    # for j in range(0, len(cache)-1):
        # print("JJJ", cache[j])
        # if cache[j]
    # if key + key == limit
    # if cache[j] +
    # return (indexsml, indexbig)
    # or return none
    print(cache)


l1 = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(l1, 5, 21))
"""
PLAN
- weights == [] list
- length == len(weights)
- limit == weight limit we are looking for
- find 2 items that sum to be `limit`
- return == (index, index) of two inecies that sum to be `limit`
- sort return statement so the smaller value is first (smaller, bigger)
- if a pair does not exist return none

- each weight in weights list can == KEY
- each weights list index can == VALUE
"""
