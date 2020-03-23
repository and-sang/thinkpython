def eval_loop():
    
    x = None
    print('Hello, I am your personal calculator')
    print('type the expression you want me to evaluate, or DONE to exit')
    while True:
        x = input('Type the expression: ')
        if x.lower() == 'done': # case-insensitive
            break
        print(f'{x} = {eval(x)}')
    
    print('That was it. Goodbye!')
    print()

if __name__ == "__main__":
    eval_loop()