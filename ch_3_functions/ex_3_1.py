import math

def right_justify(s, strlen=70):
    
    lines = 1 + (len(s) // strlen) # first line justified
    
    emptychars = (strlen - (len(s) % strlen)) * ' '
    sj = emptychars + s

    for i in range(0, len(sj), strlen):
        print(f'{sj[i:i+strlen]}') # string slices stop short of last value: sj[0:10] prints sj[0] to sj[9]

    return



if __name__ == '__main__':
    right_justify('ellaki')
    right_justify(72*'a', 10)
