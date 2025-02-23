# BOJ 14888 연산자 끼워넣기

import sys
input = sys.stdin.readline

def place_operator(nums, operator_cnt, depth, total):
    n = len(nums)
    
    if depth == n - 1:
        return total, total

    max_value, min_value = -sys.maxsize, sys.maxsize
    for i in range(4):  # 0: '+', 1: '-', 2: '*', 3: '//'
        if operator_cnt[i] > 0:  # 사용 가능한 연산자가 남아있는 경우만 진행
            next_value = total
            if i == 0:  # 덧셈
                next_value += nums[depth + 1]
            elif i == 1:  # 뺄셈
                next_value -= nums[depth + 1]
            elif i == 2:  # 곱셈
                next_value *= nums[depth + 1]
            elif i == 3:  # 나눗셈
                if next_value < 0 and nums[depth + 1] > 0:
                    next_value = -(-next_value // nums[depth + 1])  # 음수 나눗셈 처리
                else:
                    next_value //= nums[depth + 1]

            # 해당 연산자를 사용했으므로 개수를 하나 줄이고 재귀 호출
            operator_cnt[i] -= 1
            temp_max, temp_min = place_operator(nums, operator_cnt, depth + 1, next_value)
            operator_cnt[i] += 1  # 재귀 호출이 끝난 후 다시 복구

            # 최댓값, 최솟값 업데이트
            max_value = max(max_value, temp_max)
            min_value = min(min_value, temp_min)

    return max_value, min_value
    # operators = ['+'] * operator_cnt[0] + ['-'] * operator_cnt[1] + ['*'] * operator_cnt[2] + ['//'] * operator_cnt[3]

    # for i in range(len(operators)):
    #     if bitmask & (1 << i):
    #         continue

    #     new_bitmask = bitmask | (1 << i)
    #     next_value = total

    #     if operators[i] == '+':
    #         next_value += nums[depth + 1]
    #     elif operators[i] == '-':
    #         next_value -= nums[depth + 1]
    #     elif operators[i] == '*':
    #         next_value *= nums[depth + 1]
    #     elif operators[i] == '//':
    #         if next_value < 0 and nums[depth + 1] > 0:
    #             next_value = -(-next_value // nums[depth + 1])  # 음수 나눗셈 처리
    #         else:
    #             next_value //= nums[depth + 1]
        
    #     temp_max, temp_min = place_operator(nums, operator_cnt, depth + 1, next_value, new_bitmask)
    #     max_value = max(max_value, temp_max)
    #     min_value = min(min_value, temp_min)

    # return max_value, min_value

def main():
    N = int(input())
    num_list = list(map(int, input().split()))
    operator_list = list(map(int, input().split()))
    max_result, min_result = place_operator(num_list, operator_list, 0, num_list[0])
    print(max_result)
    print(min_result)

if __name__ == '__main__':
    main()