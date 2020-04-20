def print_squares(dim, nv, nh):
    h_edge = '- '
    h_body = '  '
    v_edge = '+'
    v_body = '|'

    for i in range(nv):
        print_line(dim, nh, v_edge, h_edge)
        for j in range(dim):
            print_line(dim, nh, v_body, h_body)
    print_line(dim, nh, v_edge, h_edge)
    return

def print_line(dim, nh, edge, body):
    line = nh * (edge + ' ' + dim*body) + edge    
    print(line)

if __name__ == '__main__':
    nh = 3 # n of horizontal squares
    nv = 2 # n of vertical squares
    dim = 4
    print(10*'#' + ' DIM VARIATIONS ' + 10*'#')
    for i in range(3,6,1):
        print_squares(i, 1, 1)
    print()
    print(10*'#' + ' NV VARIATIONS ' + 10*'#')
    for i in range(1,5,1):
        print_squares(dim, i, 1)
        print()
    print()
    print(10*'#' + ' NH VARIATIONS ' + 10*'#')
    for i in range(1,5,1):
        print_squares(dim, 1, i)    