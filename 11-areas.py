def sum_areas(rectangles):

    # sum = 0

    # for i in rectangles:
    #     sum += i.get("height") * i.get("width")

    # return sum

    return sum([i.get("height") * i.get("width") for i in rectangles])


rectangles = [
    { "height": 11, "width": 9,   },
    { "height": 5,  "width": 1.5, },
]

print(sum_areas(rectangles))
