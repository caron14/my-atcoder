def main():
    N, M = list(map(int, input().split()))
    C = list(map(str, input().split()))
    D = list(map(str, input().split()))
    P = list(map(int, input().split()))

    price_dict = {D[i]: P[i + 1] for i in range(M)}

    price = [price_dict.get(c, P[0]) for c in C]

    return sum(price)


if __name__ == '__main__':
    print(main())