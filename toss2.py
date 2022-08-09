# M = 20
M = 10
# load = [16,15,9,17,1,3]
load = [2,3,7,8]
load.sort(reverse=True)
trucks = [M] * len(load)
visited = [False] * len(load)
cnt = 1
start = 0
end = len(load)-1
while True:
    print(visited)
    if visited[start] == True and visited[end] == True:
        break
    
    for i in range(cnt):
        if trucks[i] >= load[start]:
            trucks[i] -= load[start]
            visited[start] = True
            start += 1
        else:
            cnt += 1
            trucks[cnt] -= load[start]
            visited[start] = True
            start += 1

        if trucks[i] >= load[end] and visited[end] is False:
            trucks[i] -= load[end]
            visited[end] = True
            end -= 1
        
        if start >= end:
            break
        
        

# while True:
#     if False not in visited:
#         break
    
#     for i in range(len(load)):
#         if trucks[cnt] >= load[i] and visited[i] is False:
#             trucks[cnt] -= load[i]
#             visited[i] = True
#         elif trucks[cnt] < load[i] and visited[i] is False:
#             cnt += 1
#             trucks[cnt] -= load[i]
#             visited[i] = True

print(cnt)