# BOJ 15903 카드 합체 놀이
import heapq
import sys

input = sys.stdin.readline

def card_game(cards):
    for _ in range(m):
        x, y = heapq.heappop(cards), heapq.heappop(cards)
        heapq.heappush(cards, x + y)
        heapq.heappush(cards, x + y)

    return sum(cards)


n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)
print(card_game(cards))