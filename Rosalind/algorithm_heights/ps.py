
def main():
    ifile = open("rosalind_ps.txt", "r")
    wfile = open("rosalind_ps_ans.txt", "w")

    n = int(ifile.readline())
    a = [int(x) for x in ifile.readline().split()]
    k = int(ifile.readline())
    print(*sorted(a)[:k], file=wfile)

if __name__ == "__main__":
    main()
