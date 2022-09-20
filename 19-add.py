def add(items):
    sum = 0
    for item in items:
        try:
            sum += float(item)
        except:
            pass
    return sum
