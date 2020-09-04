n = 1260
count = 0

list = [500, 100, 50, 10]

for coin in list:
    count = count +  (n // coin) #해당 화폐로 거슬러 줄수있는 동전의 개수 세기
    
    n = n % coin
print(count)