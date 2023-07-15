def main():
    N, M = list(map(int, input().split()))
    P, C, F = [], [], []

    for n in range(N):
        tmp = list(map(int, input().split()))
        P.append(tmp[0])
        C.append(tmp[1])
        F.append(set(tmp[2:]))

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if P[i] >= P[j]:
                if F[j] <= F[i]:
                    print(F[j] - F[i])
                    if P[i] > P[j]:
                        return 'Yes1'
                    elif F[j] - F[i]:
                        return 'Yes2'
    return 'No'


if __name__ == '__main__':
    print(main())