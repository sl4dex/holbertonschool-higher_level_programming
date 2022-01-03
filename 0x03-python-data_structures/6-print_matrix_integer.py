def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for row in matrix:
            for elem in row:
                print("{:d}".format(elem), end='')
                if elem != row[-1]:
                    print("".format(), end=' ')
            print("".format())
