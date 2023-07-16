def main():
    N = int(input())
    S = set()
    for _ in range(N):
        s = input()
        S.add(min(s, s[::-1]))
    return len(S)

if __name__ == '__main__':
    print(main())
