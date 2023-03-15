def main():
    S = list(input())
    for i in range(1, len(S) // 2 + 1):
        S[2*i - 1 - 1], S[2 * i - 1] = S[2 * i - 1], S[2*i - 1 - 1]
        
    print(''.join(S))


if __name__=='__main__':
    main()