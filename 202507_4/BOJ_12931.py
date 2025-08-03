# BOJ 12931 두 배 더하기

def is_even(list):
    for elem in list:
        if elem % 2 != 0:
            return False
    return True

def is_zero(list):
    for elem in list:
        if elem != 0:
            return False
        
    return True

N = int(input())
list_B = list(map(int, input().split()))

cnt = 0

while True:
    if is_zero(list_B):
        break
    
    # 1. 전체 2의 배수이면 반갈죽
    if is_even(list_B):
        list_B = [elem // 2 for elem in list_B]
        cnt += 1
        
    elif not is_even(list_B):
        for i in range(len(list_B)):
            if list_B[i] % 2 != 0:
                list_B[i] -= 1
                cnt += 1
                break  # 하나씩만 처리
    

print(cnt)
