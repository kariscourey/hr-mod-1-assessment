def unique_elements(items):

    # return list(set(items))  # didn't work with tests

    # result = []

    # for i in items:
    #     if i not in result:
    #         result.append(i)

    # return result

    return list({i for i in items})  # didn't work with tests, though works logically


print(unique_elements([1,1,2]))
print(unique_elements([1,1,1]))
