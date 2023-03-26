"""
s = input()
a = int(input())
b, c = map(int, input().split())
"""
import collections

def TLE(N, A):
    counter_A = collections.Counter(A)
    if N == 1:
        return 0

    ans = 0
    B = [1] * len(A)
    for i in range(len(A) - 1):
        if B[i] == -1:
            continue
        for j in range(i + 1, len(A)):
            if B[j] == -1:
                continue
            elif A[i] == A[j]:
                ans += 1
                B[i], B[j] = -1, -1
                break
    else:
        return ans

def AC(N, A):
    if N == 1:
        return 0

    counter_A = collections.Counter(A)
    ans = 0
    for key in counter_A.keys():
        while counter_A[key] > 1:
            counter_A[key] = counter_A[key] - 2
            ans += 1
    return ans

if __name__=="__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(TLE(N, A))
    print(AC(N, A))