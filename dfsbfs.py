# 백준 1260번 dfs, bfs
import sys
sys.stdin = open('dfsbfs.txt')

def dfs(S):
    print(S, end=' ')
    visited[S] = 1
    for i in range(1, N+1):
        if find_arr[S][i] == 1 and visited[i] == 0:
            dfs(i)

def bfs(S):
    que = []
    que.append(S)
    visited[S] = 1
    while que:
        S = que.pop(0)
        print(S, end=' ')
        for i in range(1, N+1):
            if find_arr[S][i] == 1 and visited[i] == 0:
                que.append(i)
                visited[i] = 1

N, M, V = map(int, input().split()) # N: 정점의 개수, M: 간선의 개수, V: 시작 노드
arr = [list(map(int, input().split())) for _ in range(M)]

# 인접 행렬 만들기
find_arr = [[0]*(N+1) for __ in range(N+1)]
for i in arr:
    find_arr[i[0]][i[1]] = 1
    find_arr[i[1]][i[0]] = 1
    
visited = [0]*(N+1)

dfs(V)
visited = [0]*(N+1)
print()
bfs(V)