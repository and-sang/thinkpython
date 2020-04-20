def do_twice(f, arg=None):
    if arg:
        f(arg)
        f(arg)
    else:        
        f()
        f()
    return   

def do_four(f, arg=None):
    do_twice(f, arg)
    do_twice(f, arg)    

def print_spam():
    print('spam')
    return

def print_twice(s):
    print(s)
    print(s)
    return

if __name__ == '__main__':
    do_twice(print_spam)
    print()
    do_twice(print_twice, 'spam')
    print()
    do_four(print_spam)
    print()
    do_four(print_twice, 'spam')