def count_entries(line, separator):
    return len(line.split(separator))

print(count_entries("a,b,c", ","))
print(count_entries("a,b,c", ";"))
