#수열을 사용해 가장 큰수의 조합을 찾고 이 횟수를 사용해 효율적으로 풀이하기
# N, M, K => 5, 8, 3
# data = 2, 4, 5, 4, 6

#N, M, K 입력받기
n, m, k = map(int, input().split())

#N개의 수를 리스트로 입력받기
data = list(map(int, input().split()))
data.sort()

first = data[-1] #가장큰수
second = data[-2] #두번째로 큰수

#가장 큰수가 더해지는 횟수 계산하기

#가장 크게 만들수있는 수열 => (6 + 6 + 6 + (5)) 그 길이는 K+1
#그 순열의 가능한 반복 횟수는 M // K+1
#순열이 2 (M // K+1)번 반복된다고 했을때 그 안에 K개의 가장큰수가 있다 => (M//(K+1)) *K
count = (m//(k+1)) *k

#만약 M이 K+1로 나누어 떨어지지 않는다면 그 나머지 만큼의 횟수는 가장큰 수로 채워지게 된다.
count += m % (k+1)

result = 0
result += (count) * first #가장큰수를 count 만큼 더하기
result += (m - count) * second #두번째로 큰수를 m - count 만큼 더하기 (총 덧셈 가능한 횟수 m 에서 가장큰수를 count 만큼 더했으므로 m - count)

print(result)

