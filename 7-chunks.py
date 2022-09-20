def make_chunks(list, size):
    chunks = []
    chunk = []
    for item in list:
        if len(chunk) == size:
            chunks.append(chunk)
            chunk = []
        chunk.append(item)
    return chunks

input = [10, 7, 3, 11, 4]

result = make_chunks(input, 3)
print(result)
