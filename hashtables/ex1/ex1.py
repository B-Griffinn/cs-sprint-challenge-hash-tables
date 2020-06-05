

def get_indices_of_item_weights(weights, length, limit):
    cache = {}

    for i in range(0, len(weights)):

        cur = weights[i]

        if cur in cache:

            needed_weight = cache[cur]

            return (i, needed_weight)

        cache[limit - cur] = i
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
