from heap2 import *
# each item of the list is a node([0]) and its edges([1:])
# for example: [1, (80, 982), (163, 8164), (170, 2620), ...]
data = []
with open("data.txt", "r") as file:
    for line in file:
        l = line.strip().split()
        edges = []
        for edge in l[1:]:
            edges.append(tuple([int(x) for x in edge.split(",")]))
        data.append([int(l[0])] + edges)


dist = [float("inf") for x in range(len(data))] # initialize all distances to be infinite
s = (1, 0) # source vertex
insert(s)
dist[s[0]-1] = 0 # distance of source vertex 

while len(heap) != 0:
    # selecting edge that minimizes the greedy criterion
    u = extract_min() # w extracted from heap

    for v in data[u[0]-1][1:]: # for each edge of v in u
        if dist[v[0]-1] > dist[u[0]-1] + v[1]:
            dist[v[0]-1] = dist[u[0]-1] + v[1]
            v_sharp = (v[0], dist[v[0]-1])
            insert(v_sharp)
    

print(dist) 