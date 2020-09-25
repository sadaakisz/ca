G=[[2, 3],
   [0],
   [],
   [4, 1],
   []]
R=[[] for _ in range(len(G))]
n=len(G)
visited=[False]*n
s=[]
ks=[]
comp=[]
def dfs(v):
    visited[v]=1
    for i in G[v]:
        if not visited[i]:
            dfs(i)
    s.append(v)
def dfs2(v):
    visited[v]=1
    ks.append(v)
    for i in R[v]:
        if not visited[i]:
            dfs2(i)
def reverseGraph():
    for i in range(len(G)):
        for j in range(len(G[i])):
            R[j].append(i)
for i in range(n):
    if not visited[i]:
        dfs(i)
reverseGraph()
visited=[False]*n
s.reverse()
for i in range(n):
    if not visited[s[i]]:
        dfs2(s[i])
        print(ks)
        comp.append(ks)
        ks.clear()