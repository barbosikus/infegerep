import heapq
n,m,k = map(int,input().split())
a = list(map(int, input().split()))
e = [list(map(int, input().split())) for i in range(m)]
def dikstra(n, m, k, a, e):
    graph = [[] for i in range(n)]
    print(graph)
    for u,v in e:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    dist = [[float('inf')]*(k+1) for i in range(n)]
    dist[0][0] = 0
    q = [(0,0,0)]
    print(dist,'\n',graph)
    rastoyaniya = []
    while q:
        cd, u, ch = heapq.heappop(q)
        if cd>dist[u][ch]:
            continue
        for v in graph[u]:
            nd = cd+abs(a[u] - a[v])
            if nd<dist[v][ch]:
                dist[v][ch] = nd
                heapq.heappush(q, (nd,v,ch))
        if ch<k:
            for v in graph[u]:
                nd = cd
                if nd < dist[v][ch+1]:
                    dist[v][ch + 1] = nd
                    heapq.heappush(q, (nd, v, ch+1))
    md = float('inf')
    bc = -1
    for i in range(k):
        if md<dist[n-1][i]:
            md = dist[n-1][i]
            bc = i
    print(dist)
    return min(dist[n-1])
print(dikstra(n,m,k,a,e))

