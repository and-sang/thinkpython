def spell_backward(s):
    '''take a string as input and display its characters backward
    '''
    i = 1
    while i <= len(s):
        print(s[-i])
        i += 1
    return

if __name__ == "__main__":
    spell_backward('banana')