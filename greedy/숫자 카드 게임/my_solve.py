#brute force
def first_try(cards):
    large_number = 0
    for card in cards:
        if large_number < min(card):
            large_number = min(card)
    
    return large_number





print(first_try([[3,1,2],[4,1,4],[2,2,2]]))
    