import numpy
from numpy import array
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

def gauss(a, b):
    a = a.copy()
    b = b.copy()

    def forward():
        n = len(a)

        for k in range(n - 1):
            for i in range(k + 1, n):
                factor = a[i][k] / a[k][k]
                for j in range(k + 1, n):
                    a[i][j] -= factor * a[k][j]
                b[i] -= factor * b[k]
                a[i][k] = 0.0

    def backward():
        x = numpy.zeros(len(b), dtype=float)
        n = len(a)
        x[n-1] = b[n-1] / a[n-1][n-1]
        for i in range(n-2, -1, -1):
            sum = b[i]
            for j in range(i+1, n):
                sum -= a[i][j] * x[j]
            x[i] = sum / a[i][i]
        return x

    forward()
    x = backward()
    return x

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

oob_solution = solve_out_of_the_box(a, b)
solution = gauss(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))
