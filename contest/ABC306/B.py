def main():
    A = list(map(int, input().split()))
    ans = [a * 2**i for i, a in enumerate(A)]

    return sum(ans)


if __name__ == '__main__':
    print(main())