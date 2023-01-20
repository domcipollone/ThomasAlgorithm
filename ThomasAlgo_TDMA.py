import numpy as np


def thomas_algorithm(lower, main, upper, b):
    """ A solver for tri-diagonal matrices, commonly referred to as the Thomas Algorithm. The function takes the values
    of the lower, main, and upper diagonal respectively, from matrix A, as floats or integers. The b argument
    represents the right hand side of Ax=b. The function returns a numpy array x, which is the solution of Ax=b.
    The matrix must be diagonally dominant for reasonable performance. |main| > |lower| + |upper|.

    Enjoy!
    """

    # if np.abs(b) < np.abs(lower) + np.abs(upper):
    #     raise Exception('Stability condition not met. The matrix is not diagonally dominant.')
    assert (np.abs(main) > (np.abs(lower) + np.abs(upper))), "The matrix must be diagonally dominant."
    number_of_rows = len(b)

    l = np.zeros(number_of_rows)
    d = np.zeros(number_of_rows)
    u = np.zeros(number_of_rows)

    l[1:] = lower
    d[:] = main
    u[:-1] = upper

    for i in range(1, number_of_rows):
        d[i] = d[i] - (l[i] / d[i - 1]) * u[i-1]

        b[i] = b[i] - (l[i] / d[i - 1]) * b[i-1]

    xn = b / d

    for i in range(number_of_rows-2, -1, -1):
        xn[i] = (b[i] - u[i] * xn[i + 1]) / d[i]

    return xn
