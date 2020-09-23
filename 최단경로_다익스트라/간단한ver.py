import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하도록 10억 설정

# 노드의 개수 n, 간선 m 입력받기
n, m = map(int, input().split())

# 시작노드번호 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기 => [[],[],[],[]...]
graph = [[] for i in range(n+1)]

# 방문 체크리스트 (True, False)
visited = [False] * (n+1)

# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 간선의 정보를 입력받기 => range(m) 간선의 개수 m 만큼 반복
#[[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
print(graph)


# 방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def dijkstara(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
