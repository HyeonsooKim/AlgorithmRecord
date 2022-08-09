"""
정렬된 배열에서 특정 수의 개수 구하기
문제
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 x가 등장하는 횟수를 계산하세요. 예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.

단, 이 문제는 시간 복잡도 O(log N)으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받습니다.

입력 조건
첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됩니다.
(1 ≤ N ≤ 1,000,000), (-10⁹ ≤ x ≤ 10⁹)

둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다.
(-10⁹ ≤ 각 원소의 값 ≤ 10⁹)

출력 조건
수열의 원소 중에서 값이 x인 원소의 개수를 출력합니다. 단, 값이 x인 원소가 하나도 없다면 -1을 출력합니다.

입력
7 2
1 1 2 2 2 2 3

출력
4

입력
7 4
1 1 2 2 2 2 3

출력
-1
"""

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index if right_index != left_index else -1

import sys
n, x = map(int, sys.stdin.readline().rstrip().split())
ls = list(map(int, sys.stdin.readline().rstrip().split()))

print(count_by_range(ls, x, x))


# 모듈을 사용하지 않는 방법
n, target = map(int, input().split())
array = list(map(int, input().split()))


def first_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (array[mid] == target) and (mid == 0 or target > array[mid - 1]):
        return mid
    elif array[mid] >= target:
        return first_search(array, target, start, mid - 1)
    else:
        return first_search(array, target, mid + 1, end)


def last_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (array[mid] == target) and (
        (mid == len(array) - 1) or (target < array[mid + 1])
    ):
        return mid
    elif array[mid] > target:
        return first_search(array, target, start, mid - 1)
    else:
        return first_search(array, target, mid + 1, end)


def count_by_value(array, x):
    n = len(array) - 1

    first_index = first_search(array, x, 0, n)

    if first_index == None:
        return 0

    last_index = last_search(array, x, 0, n)

    return last_index - first_index + 1


count = count_by_value(array, target)

if count == 0:
    print(-1)
else:
    print(count)