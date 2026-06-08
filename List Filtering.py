def filter_list(l):
    return [x for x in l if isinstance(x, int)]

y = filter_list([1,2,3,'a','b'])
print(y)
