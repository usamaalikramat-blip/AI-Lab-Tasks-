g = {"A":["B","C"],"B":["D","E"],"C":["F"],"D":[],"E":["G"],"F":[],"G":[]}
def dls(n, goal, limit, path):
    if n == goal: return "found", path
    if limit == 0: return "cutoff",[]
    cut = False
    for x in g[n]:
        if x not in path:
            s,p = dls(x, goal, limit-1, path+[x])
            if s == "found": return s, p
            if s =="cutoff": cut = True
    return ("cutoff" if cut else "failure"),[]
for i in range(1,5):
    print("DLS", i, dls("A","G",i,["A"]))
print("IDDFS")
for i in range(1,5):
    r = dls("A","G",i,["A"])
    print(i, r)
    if r[0] == "found": break
