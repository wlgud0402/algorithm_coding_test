# 메모이제이션 사용
n = int(input())

# 테이블 초기화 => 등록되지 않은것들은 값이 0
d = [0] * 30001

for i in range(2, n+1):
    # 현재의 수에서 1을 빼는 경우 => 지금 항은 전항 +1 이다
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2], +1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])
