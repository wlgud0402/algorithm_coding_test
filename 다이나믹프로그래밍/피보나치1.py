# 재귀를 통해 풀기 => 큰 문제를 해결하기위해 작은 문제를 호출 (탑다운 방식)

d = [0] * 100  # 한번 계산된 결과를 메모이제이션 하기위한 리스트 초기화


def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]


print(fibo(99))
