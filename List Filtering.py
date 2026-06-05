def filter_list(l):
    return [x for x in l if isinstance(x, int)]

x = filter_list([1,2,3,4,'a','b'])
print(x)
