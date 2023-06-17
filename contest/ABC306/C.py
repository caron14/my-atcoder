from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))

    cache = defaultdict(int)
    f = defaultdict(int)
    for i in range(3*N):
        cache[A[i]] += 1
        if cache[A[i]] == 2:
            f[i + 1] = A[i]
    keys = sorted(f)
    return ' '.join([str(f[key]) for key in keys])


if __name__=='__main__':
    print(main())