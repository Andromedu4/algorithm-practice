def filter_list(l):
    return [x for x in l if isinstance(x, int)]

yx = filter_list([1,2,3,'a','b'])
print(yx)
