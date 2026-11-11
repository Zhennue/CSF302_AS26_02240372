import heapq, random, time, csv
from pathlib import Path

def read_graph(path):
    lines=[x.strip() for x in Path(path).read_text().splitlines() if x.strip() and not x.lstrip().startswith('#')]
    n,m,source=map(int,lines[0].split()); graph=[[] for _ in range(n)]
    for line in lines[1:]: u,v,w=map(int,line.split()); graph[u].append((v,w))
    return graph,source

def dijkstra(graph,source):
    n=len(graph); dist=[float('inf')]*n; prev=[None]*n; done=[False]*n; dist[source]=0; heap=[(0,source)]
    while heap:
        d,u=heapq.heappop(heap)
        if done[u]: continue
        done[u]=True
        for v,w in graph[u]:
            if not done[v] and d+w<dist[v]: dist[v]=d+w; prev[v]=u; heapq.heappush(heap,(dist[v],v))
    return dist,prev

def path_to(prev,s,t):
    path=[]; cur=t
    while cur is not None:
        path.append(cur)
        if cur==s:return path[::-1]
        cur=prev[cur]
    return []

class DSU:
    def __init__(self,n): self.p=list(range(n)); self.rank=[0]*n
    def find(self,x):
        if self.p[x]!=x:self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,a,b):
        a=self.find(a); b=self.find(b)
        if a==b:return False
        if self.rank[a]<self.rank[b]:a,b=b,a
        self.p[b]=a
        if self.rank[a]==self.rank[b]:self.rank[a]+=1
        return True

def kruskal(n,edges):
    d=DSU(n); total=0; chosen=[]
    for w,u,v in sorted(edges):
        if d.union(u,v):
            total+=w; chosen.append((u,v,w))
            if len(chosen)==n-1:break
    if len(chosen)!=n-1:raise ValueError('Graph disconnected')
    return total,chosen

def prim(n,adj):
    seen=[False]*n; heap=[(0,0,-1)]; total=0; chosen=[]
    while heap and len(chosen)<n-1:
        w,u,parent=heapq.heappop(heap)
        if seen[u]:continue
        seen[u]=True; total+=w
        if parent!=-1:chosen.append((parent,u,w))
        for v,cost in adj[u]:
            if not seen[v]:heapq.heappush(heap,(cost,v,u))
    if len(chosen)!=n-1:raise ValueError('Graph disconnected')
    return total,chosen

def make_graph(n,edge_count,seed):
    r=random.Random(seed); weights={}
    for v in range(1,n):
        u=r.randrange(v); weights[(u,v)]=r.randint(1,1000)
    target=min(n*(n-1)//2,edge_count)
    while len(weights)<target:
        u,v=r.sample(range(n),2)
        if u>v:u,v=v,u
        weights[(u,v)]=r.randint(1,1000)
    edges=[(w,u,v) for (u,v),w in weights.items()]; adj=[[] for _ in range(n)]
    for w,u,v in edges:adj[u].append((v,w));adj[v].append((u,w))
    return edges,adj

def benchmark():
    n=1000; rows=[]
    for label,m in [('sparse',3*n),('dense',n*(n-1)//4)]:
        edges,adj=make_graph(n,m,700+n)
        t=time.perf_counter(); kw,_=kruskal(n,edges); kt=time.perf_counter()-t
        t=time.perf_counter(); pw,_=prim(n,adj); pt=time.perf_counter()-t
        assert kw==pw
        print(f'{label.title()} graph V={n}, E={len(edges)} | Kruskal={kt:.4f}s | Prim={pt:.4f}s | MST weight={kw}')
        rows.append([label,n,len(edges),kt,pt,kw])
    out=Path(__file__).parent/'outputs'/'q3_mst_benchmark.csv'
    with out.open('w',newline='') as f:w=csv.writer(f);w.writerow(['type','V','E','kruskal_seconds','prim_seconds','mst_weight']);w.writerows(rows)
    print('Saved',out)

if __name__=='__main__':
    base=Path(__file__).parent; graph,source=read_graph(base/'directed_graph.txt'); dist,prev=dijkstra(graph,source)
    print('Q3.1 Dijkstra shortest paths')
    for v,d in enumerate(dist):print(f'Vertex {v}: distance={d}, path={path_to(prev,source,v) or "unreachable"}')
    print('\nQ3.2/3.3 Random connected graph verification')
    for i in range(10):
        edges,adj=make_graph(30,100,372+i); a,_=kruskal(30,edges); b,_=prim(30,adj); assert a==b
    print('Kruskal and Prim produced the same MST weight on 10/10 random connected graphs.')
    print('\nQ3.4 Performance benchmark, V=1000'); benchmark()
    print('\nQ3.5 Negative edge demonstration')
    bad=[[(1,2),(2,5)],[],[(1,-10)]]; result,_=dijkstra(bad,0)
    print('Edges: 0->1 (2), 0->2 (5), 2->1 (-10)')
    print('Dijkstra distance to vertex 1:',result[1],'; actual shortest distance: -5 via 0->2->1')
    print('Dijkstra fails because it finalizes vertex 1 before the negative edge is processed.')
