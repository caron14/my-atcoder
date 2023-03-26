def main(N, W, test_case):
    for w in W:
        if w in test_case:
            return "Yes"
    return "No"


if __name__=="__main__":
    test_case = ["and", "not", "that", "the", "you"]
    N = int(input())
    W = list(map(int, input().split()))
    print(main(N, W, test_case))