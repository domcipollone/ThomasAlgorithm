# ThomasAlgorithm

A solver for tri-diagonal matrices, commonly referred to as the Thomas Algorithm. The function takes the values
of the lower, main, and upper diagonal respectively, from matrix A, as floats or integers. The b argument
represents the right hand side of Ax=b. The function returns a numpy array x, which is the solution of Ax=b.
The matrix must be diagonally dominant for reasonable performance. |main| > |lower| + |upper|.

Enjoy!
