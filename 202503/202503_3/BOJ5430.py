# BOJ 5430 AC
from collections import deque
import sys
input = sys.stdin.readline

def AC():
    is_reversed = False
    for command in commands:
        if command == 'R':
            is_reversed = not is_reversed
        elif command == 'D':
            if not numbers:
                print("error")
                return
            if is_reversed:
                numbers.pop()
            else:
                numbers.popleft()
        
    if is_reversed:
        numbers.reverse()

    print('[', end='')
    print(*numbers, sep=',', end='')
    print(']')


T = int(input())
for _ in range(T):
    commands = input()
    n = int(input())
    numbers = input().strip()[1:-1]
    numbers = deque() if n == 0 else deque(numbers.split(','))
    AC()