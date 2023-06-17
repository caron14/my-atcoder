def main():
    N = int(input())
    S = input()
    ans = []
    for s in S:
        ans.append(s+s)

    return ''.join(ans)


if __name__=='__main__':
    print(main())