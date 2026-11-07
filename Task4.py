import heapq
g = {"S":[("A",1),("B",4)],"A":[("C",2)],
     "B":[("G",5)], "C":[("G",3)], "G":[]}
h = {"S":5,"A":4,"B":4,"C":2,"G":0}
def search(heuristic):
    q = [(heuristic["S"],0,"S",["S"])]
    best = {"S":0}
    expanded = []
    while q:
        f,c,n,p = heapq.heappop(q)
        if c != best[n]:
             continue
        if n == "G":
            return p,c,expanded
        expanded.append(n)
        for x,w in g[n]:
            nc = c+w
            if nc < best.get(x,float("inf")):
                best[x] = nc
                heapq.heappush(q,(nc+heuristic[x],nc,x,p+[x]))
    return None
print("A*:", search(h))
print("UCS:", search(dict.fromkeys(h,0)))
h["C"] = 10
print("Modified A*:", search(h))
