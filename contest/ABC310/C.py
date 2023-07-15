def are_strings_equal(string1, string2):
    return hash(string1) == hash(string2)


def main():
    N = int(input())
    S, S_r = [], []
    for _ in range(N):
        s = input()
        S.append(s)
        S_r.append(s[::-1])

    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            # if S[i] == S[j]:
            if are_strings_equal(S[i], S[j]):
                break
            # elif S[i] == S_r[j]:
            elif are_strings_equal(S[i], S_r[j]):
                break
        else:
            cnt += 1
    return cnt

if __name__ == '__main__':
    print(main())
