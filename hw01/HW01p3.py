
def mask_x(ary, xmin, xmax):
    outarray = []

    for x in ary:
        if x >= xmin and x <= xmax:
            outarray.append(True)
        else:
            outarray.append(False)

    return outarray

print(mask_x([1.9, 3.3, 4.0, 4.1], 2.1, 4.1))