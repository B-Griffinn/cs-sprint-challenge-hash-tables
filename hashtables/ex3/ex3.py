def intersection(arrays):
    # create cache
    cache = {}

    result = []

    # word count approach
    for i in arrays:
        for j in i:
            if j in cache:
                cache[j] += 1
            else:
                cache[j] = 1
    for x in cache:
        if cache[x] > 1:
            result.append(x)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1, 4)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))


"""
PLAN
- use word count approach
- return number that has a value > 1
"""
