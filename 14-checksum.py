def checksum(message):

    # sum = 0

    # for i in message:
    #     sum += ord(i)

    # return chr(sum % 26 + 97)

    return chr(sum([ord(i) for i in message]) % 26 + 97)


print(checksum("bat"))
print(checksum("cat"))
print(checksum("hack reactor"))
