
# create cache
cache = {}


def finder(files, queries):

    # create result arr
    result = []

    # loop thru file arr and add to cache when necessary
    for i in files:
        if i not in cache:
            cache[i] = i

    for j in cache:
        # print("JJJJJJ ", j)
        for x in queries:
            # print("XXXXXXXXXXXX ", x)
            if x in j:
                result.append(j)
                # print("RRRRRRRRRR", result)
    return result


if __name__ == "__main__":
    files = ['/dir256/dirb256/file256',
             '/dir256/file256', '/dir3490/dirb3490/file3490',
             '/dir3490/file3490', '/dir8192/dirb8192/file8192',
             '/dir8192/file8192']
    queries = [
        "file3490",

        "file8192"
    ]
    print(finder(files, queries))


"""
PLAN
- we only need check if the text after the last `/` == our query index
"""
