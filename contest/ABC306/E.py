def main():
    N, K, Q = map(int, input().split())
    A = [0] * N

    for _ in range(Q):
        X, Y = map(int, input().split())
        A[X - 1] = Y
        B = sorted(A, reverse=True)
        print(sum(B[:K]))


if __name__=='__main__':
    main()
    # Input
    # 4 2 10
    # 1 5
    # 2 1
    # 3 3
    # 4 2
    # 2 10
    # 1 0
    # 4 0
    # 3 1
    # 2 0
    # 3 0
    # Output
    # 5
    # 6
    # 8
    # 8
    # 15
    # 13
    # 13
    # 11
    # 1
    # 0