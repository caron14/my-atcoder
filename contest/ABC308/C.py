"""
TLE
"""


import sys
from fractions import Fraction

def main():
    N = int(input())

    ans = {}
    input_data = sys.stdin.readlines()
    for i in range(N):
        A, B = map(int, input_data[i].split())
        p = Fraction(A, A + B)  # 有理数として成功率を表現
        if p not in ans:
            ans[p] = [str(i + 1)]
        else:
            ans[p].append(str(i + 1))

    ans_s = sorted(ans, reverse=True)
    ret = [ans[key] for key in ans_s]

    return ' '.join([' '.join(values) for values in ret])

if __name__ == '__main__':
    print(main())
