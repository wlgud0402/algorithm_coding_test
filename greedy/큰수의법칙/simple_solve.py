#간단하게 풀이하기 but 입력량이 많아질수록 부담이 커지고 시간초과 날 확률이 놓다

#N, M, K 입력받기
n, m, k = map(int, input().split())

#N개의 수를 리스트로 입력받기
data = list(map(int, input().split()))
data.sort()

first = data[-1] #가장큰수
second = data[-2] #두번째로 큰수

result = 0
while True:
    for i in range(k): #가장 큰수를 k번 더하기 
        if m == 0: #모든 횟수를 더했다면 => m == 0 
            break
        result += first
        m -= 1 #더할때마다 count -1
    
    if m == 0:
        break
    result += second #두번째로 큰수를 한번 더하기
    m -= 1