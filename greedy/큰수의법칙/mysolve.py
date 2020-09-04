#배열 크기 5
#숫자 더하는 횟수 8번
# 같은숫자 3 번까지 더하기 가능

array = [2,4,5,4,6]
#666 5 666 5
import copy
def mysolve(count , same_count , array):
    array.sort()
    new_same_count = copy.deepcopy(same_count)
    answer = 0
    for _ in range(count):
        if count == 0:
            return answer
        
        if new_same_count == 0:
            answer += array[-2]
            count -= 1
            new_same_count =  copy.deepcopy(same_count)
            print("new_same_count즉 같은 횟수를 다사용했을때=> 두번째로 큰수 :", array[-2], "answer: ", answer)
            continue

        if new_same_count != 0:
            answer += array[-1]
            count -= 1
            new_same_count -= 1
            print("same count가 남았음 => 가장큰수 :",array[-1], "answer: " ,answer)
            continue
    return answer

print(mysolve(8, 3, [2,4,5,4,6]))


