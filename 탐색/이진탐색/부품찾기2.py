# 계수정렬의 개념을 이용한 풀이법
N = int(input())
array = [0]*10


# 가게의 전체 부품번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1
print(array)

# 손님이 원하는 목록 입력받기
M = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
