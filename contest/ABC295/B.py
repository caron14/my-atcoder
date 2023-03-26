"""
s = input()
a = int(input())
b, c = map(int, input().split())
"""
def bomb(B, i, j, R, C):
    scale = int(B[i][j])
    for k in range(R):
        for l in range(C):
            dis = abs(i - k) + abs(j - l)
            if dis <= scale and B[k][l] in ["#", "."]:
                B[k][l] = "."
    return B

def main():
    # retrieve input
    R, C = map(int, input().split())
    B = []
    for _ in range(R):
        B.append(list(input()))

    for i in range(R):
        for j in range(C):
            if B[i][j] not in ["#", "."]:
                B = bomb(B, i, j, R, C)
                B[i][j] = "."

    for b in B:
        print("".join(b))
        

if __name__=="__main__":
    main()