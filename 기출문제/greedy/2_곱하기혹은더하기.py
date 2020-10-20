def solution(str_num):
    nums = [int(num) for num in str_num]
    answer = 1
    for i in range(0, len(nums)):
        if nums[i] == 0 or nums[i] == 1:
            answer += nums[i]
        else:
            answer *= nums[i]

    print(answer)


print(solution("567"))
