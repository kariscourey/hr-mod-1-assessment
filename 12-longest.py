def find_longest(lists):

    # if lists:
    #     return max(lists, key=len)

    if lists:

        max = lists[0]

        for i in lists:
            if len(i) > len(max):
                max = i

        return max

lists = [[1], [1,2,3], [1,2]]

print(find_longest(lists))
