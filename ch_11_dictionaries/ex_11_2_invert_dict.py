def main():
    d = {1:'a', 2:'b', 3:'b', 4:'c'}
    print(invert_dict(d))
    print(invert_dict_concise(d))

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def invert_dict_concise(d):
    inverse = dict()
    for key in d:
        # val = d[key]
        inverse.setdefault(d[key], []).append(key)
    return inverse


if __name__ == "__main__": main()