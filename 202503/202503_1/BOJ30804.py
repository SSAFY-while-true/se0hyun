# BOJ 30804 과일 탕후루

from collections import Counter
import sys
input = sys.stdin.readline

def make_fruit_skewer(n, fruits):
    left, right = 0, 2
    max_len = 2
    fruit_count = {fruits[0]: 1, fruits[1]: 1, fruits[2]: 1}
    while right < n:
        if (len(fruit_count) <= 2):
            max_len = max(max_len, right - left + 1)
            right += 1
            if right < n:
                fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1
        else:
            if fruits[left] in fruit_count:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
            left += 1
    return max_len

def main():
    N = int(input())
    fruit_list = list(map(int, input().split()))
    print(make_fruit_skewer(N, fruit_list))

if __name__=='__main__':
    main()