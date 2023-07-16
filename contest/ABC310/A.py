def main():
    N, P, Q = list(map(int, input().split()))
    D = list(map(int, input().split()))
    tot = [P]
    for d in D:
        tot.append(Q + d)

    return min(tot)

if __name__=='__main__':
    print(main())