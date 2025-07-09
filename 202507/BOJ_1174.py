# BOJ 1174 줄어드는 수
from itertools import combinations


def get_decreasing_num(N):
    answers = []
    for mask in range(1, 1024):
        selected = []
        for digit in range(10):
            if mask & (1 << digit):
                selected.append(digit)

        selected.sort(reverse=True)
        answers.append(int("".join(map(str, selected))))
    answers.sort()
    if N > len(answers):
        return -1
    else:
        return answers[N - 1]


if __name__ == "__main__":
    N = int(input())
    print(get_decreasing_num(N))
