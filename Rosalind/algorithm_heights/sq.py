def multiply(a, b):

    lena = len(a)
    c = [[0] * lena for _ in range(lena)]
    for i in range(lena):
        for j in range(lena):
            for k in range(lena):
                c[i][j] += a[i][k] * b[k][j]
    return c

def has_sqr(adj):
    mult_matrix = multiply(adj, adj)

    print( any([i != j and mult_matrix[i][j] > 1 for j in len(mult_matrix) for i in len(mult_matrix)]))

def main():
    ifile = open("rosalind_sq.txt", "r")
    wfile = open("rosalind_sq_ans.txt", "w")

    for _ in range(int(ifile.readline())):

        ifile.readline()
        n, e = [int(x) for x in ifile.readline.split()]
        adj = [[0 for x in range(n)] for y in range(n)]
        for _ in range(e):
            u, v = [int(x) for x in ifile.readline.split()]
            adj[u-1][v-1] = 1
            adj[v-1][u-1] = 1
        print( 1 if has_sqr(adj) else -1, end=" ")
        print( 1 if has_sqr(adj) else -1, end=" ", file = wfile)



