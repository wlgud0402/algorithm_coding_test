n, m = map(int, input().split())

result = 0
#한줄씩 입력받기 => n행이기때문에 n번
for i in range(n):
    data = list(map(int, input().split())) #데이터를 리스트에 담기

    #입력받은 행의 가장 작은 수
    min_value = min(data)

    #가장 작은 수 들중에서 가장 큰수 찾기
    result = max(result, min_value)

print(result)
