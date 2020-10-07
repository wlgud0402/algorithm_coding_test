from datetime import timedelta


def solution(n):
    time = timedelta(hours=n+1) - timedelta(seconds=1)
    time_list = [time]
    d = 1
    while time_list[-1] != timedelta(hours=0):
        div_time = time - timedelta(seconds=d)
        time_list.append(div_time)
        d += 1

    time_list = [str(i) for i in time_list]
    count = 0
    for str_time in time_list:
        if str(n) in str_time:
            count += 1
    return count


print(solution(5))
# 시간: 00:00:00
