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
            print(distance[i], "<", min_value)
            min_value = distance[i]
            index = i

    return index


def dijkstara(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        print("graph[start]:", graph[start], "j: ", j,
              "distance[j[0]]: ", distance[j[0]], "j[1]: ", j[1])
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for _ in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다르 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstara(start)

# 모든 노드로 가기 위한 최단거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우 "INFINITY"를 출력
    if distance[i] == INF:
        print("INFINITY")

    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
