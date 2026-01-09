


# Matrix Multiplication using Divide and Conquer Method...

def add_mul(a, b, result_mat, mid):

    for x in range(mid):

        for y in range(mid):

            result_mat[x][y] = a[x][y] + b[x][y]

def fill_zero(c, n):

    for x in range(n):
        y = []

        for z in range(n):
            y.append(0)

        c.append(y)


def mat_mul(mat_1, mat_2):

    if (len(mat_1) != len(mat_2)) or ((len(mat_1) % 2) != 0):

        return "Matrix are not Same"
    
    # Result Matrix.....
    n = len(mat_1)
    result_mat = []

    # Filling the final result matrix with zeros....
    fill_zero(result_mat, n)

    # If the Matrix is 2 by 2 then it will matiply else it will continue to divide.....
    if len(mat_1) == 2:

        for i in range(n):
        
            for j in range(n):

                result_mat[i][j] = 0

                for z in range(n):

                    result_mat[i][j] = result_mat[i][j] + (mat_1[i][z] * mat_2[z][j])
        

    else:

        mid = len(mat_2) // 2

        a = []
        b = []
        c = []
        d = []
        e = []
        f = []
        g = []
        h = []
        r1 = []
        r2 = []
        r3 = []
        r4 = []

        fill_zero(a, mid)
        fill_zero(b, mid)
        fill_zero(c, mid)
        fill_zero(d, mid)
        fill_zero(e, mid)
        fill_zero(f, mid)
        fill_zero(g, mid)
        fill_zero(h, mid)
        fill_zero(r1, mid)
        fill_zero(r2, mid)
        fill_zero(r3, mid)
        fill_zero(r4, mid)


        # Filling the Values of Orginal Matrix to the Divide Matrix....
        for i in range(mid):

            for j in range(mid):

                # First Matrix Dividing....
                a[i][j] = mat_1[i][j]   # First Block....
                b[i][j] = mat_1[i][mid + j]  # Second Block....
                c[i][j] = mat_1[mid + i][j]  # Third Block...
                d[i][j] = mat_1[mid + i][mid + j] # Fourth Block....

                # Second Matrix Dividing....
                e[i][j] = mat_2[i][j]   # First Block....
                f[i][j] = mat_2[i][mid + j]  # Second Block....
                g[i][j] = mat_2[mid + i][j]  # Third Block...
                h[i][j] = mat_2[mid + i][mid + j] # Fourth Block....


        # [  (ae + bg),  (af + bh)  ]
        # [  (ce + dg),  (cf + dh)  ]

        # add_mul(a, b, result_mat, mid):
        
        add_mul(mat_mul(a, e), mat_mul(b, g), r1, mid)
        add_mul(mat_mul(a, f), mat_mul(b, h), r2, mid)
        add_mul(mat_mul(c, e), mat_mul(d, g), r3, mid)
        add_mul(mat_mul(c, f), mat_mul(d, h), r4, mid)


        for i in range(mid):

            for j in range(mid):

                result_mat[i][j] = r1[i][j]
                result_mat[i][mid + j] = r2[i][j]
                result_mat[mid + i][j] = r3[i][j]
                result_mat[mid + i][mid + j] = r4[i][j]


    return result_mat
            

        

# Max 4 by 4 Mul....


# 4 by 4 Matrix Multiplication.....
A = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
B = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]

# A = [[1, 1, 1, 1], [2, 2, 2, 2]]
# B = [[1, 1, 1, 1], [2, 2, 2, 2]]

result = mat_mul(A, B)

print(result)

