def solution(string):
    string = list(string)
    string.sort()
    print(string)

    num = ""
    answer = []
    for i in range(len(string)):
        try:
            int_num = int(string[i])
            num += str(int_num)
        except:
            answer.append(string[i])

    return ''.join(answer) + num


print(solution("ABCDE123"))
