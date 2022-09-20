def count_matches(items, match=None):
    matches = []
    for item in items:
        if(item.get("background") == match):
            matches.append(item)
    return len(matches)

input = [
    {"background": "green",  "color": "blue", "size": 5},
    {"color": "green", "size": 5, "weight": "heavy"},
    {"background": "yellow", "size": 5,  "weight": "light"},
    {"color": "blue", "size": 25, "weight": "light"},
]

result = count_matches(input)
print(result)
