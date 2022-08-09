# 연속되는 번호
skills1 = [3, 2, 4, 1]
team1 = [2, 4]
k1 = 3

skills2 = [1, 1, 4, 2, 1, 1]
team2 = [2, 1, 5]
k2 = 4

skills3 = [5, 8, 3, 1]
team3 = [4, 3]
k3 = 2

from itertools import combinations

def solution(skills, team, k):
    ls = [[j for j in range(i, i+k)] for i in range(len(skills)-k+1)]
    sum_list = []
    team = [i-1 for i in team]
    sum_list = [sum(skills[i[0]:i[0]+len(i)]) * 2 if set(team).issubset(set(i)) else sum(skills[i[0]:i[0]+len(i)]) for i in ls]
    answer = max(sum_list)
    return answer

import time

st = time.time()
solution(skills2, team2, k2)
en = time.time()

print(en-st)