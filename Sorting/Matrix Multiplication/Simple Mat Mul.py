
# Simple Matrix Mulitplication....

def simple_mat_mul(a, b, n):

    # c = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    c = []

    
    # Fill C matrix with zero values... Or it will give index out of range error...
    for x in range(n):
        y = []
        for q in range(n):
            y.append(0)
            
        c.append(y)

    #    A              B
    # [ a, b ]   *   [ e, f ]   => [  (ae + bg),  (af + bh)  ]
    # [ c, d ]       [ g, h ]      [  (ce + dg),  (cf + dh)  ]

    
    for i in range(n):
        
        for j in range(n):

            c[i][j] = 0

            for z in range(n):

                c[i][j] = c[i][j] + (a[i][z] * b[z][j])

    return c



# Max 4 by 4 Matrix Multiplication.....
                
# 4 by 4 Matrix Multiplication.....
A = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
B = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]

# 2 by 2 Matrix Multiplication....
# A = [[1, 1, 1, 1], [2, 2, 2, 2]]
# B = [[1, 1, 1, 1], [2, 2, 2, 2]]


C = simple_mat_mul(A, B, len(A))
print(C)

