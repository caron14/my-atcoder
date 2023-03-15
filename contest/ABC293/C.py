import itertools


def main():
    H, W = list(map(int, input().split()))
    mat = []
    for i in range(H):
        mat.append(list(map(int, input().split())))
    
    h_step = [0] * (H - 1)
    w_step = [1] * (W - 1)
    
    step_cand = set(itertools.permutations(h_step + w_step))
    ans = 0
    hh = {0:1, 1:0}
    ww = {0:0, 1:1}
    for step in step_cand:
        h, w = 0, 0
        cache = set([mat[h][w]])
        for id in step:
            h += hh[id]
            w += ww[id]
            if mat[h][w] in cache:
                break
            else:
                cache.add(mat[h][w])
        else:
            ans += 1
    print(ans)


if __name__=='__main__':
    main()
