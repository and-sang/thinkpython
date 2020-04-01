def nested_sum(li):
    '''takes a list of lists of integers and return the sum of all their elements
    '''
    t = li[:]
    flat = flatten_list(t)
    return list_reduce(flat)

def flatten_list(li):
    '''takes a list of lists of integers and flatten it to a list of integeres
    '''
    res = []
    t = li[:]
    for element in t:
        if isinstance(element, list):
            res += flatten_list(element)
        else:
            res.append(element)
    return res

def list_reduce(li):
    '''traverses the list and accumulates its elements into a single result
    '''
    t = li[:]
    res = 0
    while t:
        res += t.pop()
    return res

if __name__ == "__main__":
    print(flatten_list([1, [2, 3], 4, [5, 6, [7, 8, 9]]]))
    print(list_reduce([1, 2, 3, 4]))
    print(nested_sum([1, [2, 3], 4, [5, 6, [7, 8, 9]]]))
    