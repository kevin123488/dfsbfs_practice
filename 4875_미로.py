# N*N 크기 미로에서 출발지에서 목적지에 도착하는 경로가 존쟇는지 확인하는 프로그램을 작성하라.
# 도착 가능하면 1, 아니면 0 출력

import sys
sys.stdin = open('4875.txt')

# 델타탐색, 우좌하상
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(a, b):
    global ans
    visited[a][b] = 1 # 방문기록
    if arr[a][b] == 3:
        ans = 1
        return
    for i in range(4): # 델타탐색 시작
        ni = a + di[i]
        nj = b + dj[i]
        if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0 and arr[ni][nj]!=1:
            dfs(ni, nj)
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = [[0]*N for __ in range(N)]
    ans = 0
    # 출발점 찾기
    for i in range(N): # N*N arr
        for j in range(N):
            if arr[i][j] == 2: # 출발점일 때
                dfs(i, j)
                print(f'#{tc} {ans}')
                print(visited)