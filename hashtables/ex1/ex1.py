def get_indices_of_item_weights(weights, length, limit):
    # creat a cache
    cache = {}

    # loop through the len of our weights arr so we can extract each index value
    for i in range(0, len(weights)):
        # create a cur variable to track our weight index value
        cur = weights[i]
        # print(cur)

        # if our weight index value is already in the cache...
        if cur in cache:
            # then we need to store that index in a variable that is to be returned as a tuple
            needed_weight = cache[cur]
            # print(needed_weight)
            # returning our tuple using the found indecies
            return (i, needed_weight)

        # subract limit from curent value in each cache index and set it to i so that this opperation is conducted each loop
        cache[limit - cur] = i
    # return none if we can not merge packages
    return None


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
