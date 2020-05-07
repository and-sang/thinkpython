def main():
    tu = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    tv = (1, 2, 3, 9, 5, 6, 7, 8, 9)
    print(has_duplicates(tu))
    print(has_duplicates(tv))


def has_duplicates(li):
    d = dict()
    for item in li:
        if item not in d:
            d[item] = ''
        else:
            return True
    return False


if __name__ == "__main__": main()