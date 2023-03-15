def main():
    N = int(input())
    A = list(map(int, input().split()))

    cache = set()
    for i in range(1, N + 1):
        if i not in cache:
            cache.add(A[i - 1])
    ans = [str(i) for i in range(1, N + 1) if i not in cache]
    print(len(ans))
    print(' '.join(ans))


if __name__ == '__main__':
    main()