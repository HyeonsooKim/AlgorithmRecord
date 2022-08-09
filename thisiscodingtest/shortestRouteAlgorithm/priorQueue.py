# 우선순위 큐
# 다익스트라는 선형탐색이기 때문에 노드가 5000개 이하면 사용해도 좋지만, 10000개를 넘어갈 경우 우선순위 큐를 사용해야함
# 우선순위 큐는 최소 힙 또는 최대 힙을 사용함
import heapq # min heap만 있음

# 오름차순 힙 정렬(Heap sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


# 내림차순 힙 정렬(Heap sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)