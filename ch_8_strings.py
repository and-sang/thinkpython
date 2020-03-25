def spell_backward(s):
    '''take a string as input and display its characters backward
    '''
    i = 1
    while i <= len(s):
        print(s[-i])
        i += 1
    return

def make_way():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    print('Make way for ducklings!')
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            print(letter + 'u' + suffix)
        else:
            print(letter + suffix)
    return

if __name__ == "__main__":
    # spell_backward('banana')
    make_way()