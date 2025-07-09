# Programmers 이모티콘 할인행사
def make_disc_list(emoticons):
    rates = [10, 20, 30, 40]
    discounts = []
    
    for mask in range(4 ** len(emoticons)):
        combos = []
        for i in range(len(emoticons)):
            rate_idx = (mask >> (i * 2)) & 0b11
            combos.append(rates[rate_idx])
        discounts.append(combos)
    
    return discounts
    
def solution(users, emoticons):
    answer = [0, 0]
    rates = make_disc_list(emoticons)
    
    for rate in rates:    
        plus, profit = 0, 0
        for user in users:
            total = 0
            for i in range(len(emoticons)):
                if rate[i] >= user[0]:
                    total += int(emoticons[i] * (100-rate[i])) / 100
            if total >= user[1]:
                plus += 1
            else:
                profit += total
        if plus > answer[0] or (plus == answer[0] and profit > answer[1]):
            answer[0], answer[1] = plus, profit
            
    return answer