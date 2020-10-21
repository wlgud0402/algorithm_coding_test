def solution(score):
    score = [int(i) for i in str(score)]
    mid = len(score)//2

    left = sum(score[:mid])
    right = sum(score[mid:])

    if left == right:
        return "LUCKY"
    else:
        return "READY"


print(solution(123402))
