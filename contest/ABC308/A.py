def main():
    S = list(map(int, input().split()))
    _tmp = 0
    for s in S:
        if s < _tmp:
            return "No"
        if (s < 100) or (s > 675):
            return "No"
        if s % 25 != 0:
            return "No"
        _tmp = s

    return 'Yes'


if __name__=='__main__':
    print(main())