# 풀지 못한 문제
"""
미래 도시
[문제]
미래 도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다.

 

방문 판매원 A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 한다.

 

미래 도시에서 특정 회사에 도착하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일하다.

 

또한 연결된 2개의 회사는 양방향으로 이동할 수 있다. 공중 미래 도시에서 특정 회사와 다른 회사가 도로로 연결되어

 

있다면, 정확히 1만큼의 시간으로 이동할 수 있다.

 

또한 오늘 방문 판매원 A는 기대하던 소개팅에도 참석하고자 한다. 소개팅의 상대는 K번 회사에 존재한다.

 

방문 판매원 A는 X번 회사에 가서 물건을 판매하기 전에 먼저 소개팅 상대의 회사에 찾아가서 함께 커피를 마실 예정이다.

 

따라서 방문 판매원 A는 1번 회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는 것이 목표다.

 

이때 방문 판매원 A는 가능한 한 빠르게 이동하고자 한다. 

 

방문 판매원이 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오.

 

[입력 조건]
1. 첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례대로 주어진다. (1 <= N, M <= 100)

 

2. 둘째 줄부터 M + 1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.

 

   M + 2번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다. (1 <= K <= 100)

 

[출력 조건]
1. 첫째 줄에 방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다.

 

2. 만약 X번 회사에 도달할 수 없다면 -1을 출력한다.

<입력 예시 1>
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
<출력 예시 1>
3

<입력 예시 2>
4 2
1 3
2 4
3 4
<출력 예시 2>
-1
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
INF = int(1e9)
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

print(graph)
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append((b, 1))

x, k = map(int, input().rstrip().split())

import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

print(distance)

# 해결 방법 - 플로이드 워셜 사용
n, m = map(int, input().split())

INF = int(1e9)
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1) :
  for b in range(1, n + 1) :
    if a == b :
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m) :
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1) :
  for a in range(1, n + 1) :
    for b in range(1, n + 1) :
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

if distance >= INF :
  print("-1")
else :
  print(distance)