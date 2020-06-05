def has_negatives(a):
    cache = {}

    result = []

    for i in a:
        print("I", i)
        if i not in cache:
            cache[i] = i

    for j in cache:
        print('cache[j]', cache[j])
        if cache[j] < 0 and cache[j] in cache:
            result.append(abs(cache[j]))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


"""
use the `abs` method to check if nums are ==
- create a cache
- if not 
"""
