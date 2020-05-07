def cumsum(li):
    '''takes a list of numbers and return a list of their cumulative sum
    '''
    res = li[:1]
    for el in li[1:]:
        if isinstance(el, int) r isinstance(el, float):
            res.append(el + res[-1])
    return res


if __name__ == "__main__":
    print(cumsum([1., 1, 1, 1]))