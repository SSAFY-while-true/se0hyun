# BOJ 3621 족보

def main():
    n, d = map(int, input().split())    # 외계인 개수, 부모 수
    child_list = list(map(int, input().split()))

    parents_cnt = [0 for _ in range(n + 1)]
    result = 0

    for i in child_list:
        parents_cnt[i] += 1

    for child in parents_cnt:
        while child > d:
            result += 1
            child = child - d + 1

    print(result)
if __name__ == '__main__':
    main()