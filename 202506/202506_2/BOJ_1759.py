# BOJ 1759 암호 만들기
from itertools import combinations, product

L, C = map(int, input().split())
chars = list(input().split())
consonants = chars.copy()
vowels = []

for v in ['a', 'e', 'i', 'o', 'u']:
    if v in consonants:
        consonants.remove(v)
        vowels.append(v)

results = []

for vowel_count in range(1, L-1):
    if vowel_count > len(vowels):
        break
    con_count = L - vowel_count
    vowel = list(combinations(vowels, vowel_count))
    consonant = list(combinations(consonants, con_count))
    
    # print(vowel)
    # print(consonant)
    
    results += [''.join(sorted(item1 + item2)) for item1, item2 in product(vowel, consonant)]
    
results.sort()
print(*results, sep='\n')
        