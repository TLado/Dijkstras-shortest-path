from random import randint
from time import sleep
# Array implementation of heap data structure
heap = [] # main array
def get_parent(i):
    return i//2

def bubble_up():
    i = len(heap)-1
    p = get_parent(i)
    while heap[p][1] > heap[i][1]:
        heap[i], heap[p] = heap[p], heap[i] # swapping parent and child
        i = p
        p = get_parent(i)

def insert(k):
    heap.append(k)
    bubble_up()

def get_children(p):
    i1 = i2 = p # if has no child return itself
    l = len(heap)-1 # last index
    if l >= 2*p+1:
        i1 = 2*p+1
    if l >= 2*p+2:
        i2 = 2*p+2
    if heap[i1][1] > heap[i2][1]:
        return i2
    else:
        return i1

def bubble_down():
    p = 0 # root
    i = get_children(p)
    while heap[p][1] > heap[i][1]:
        heap[i], heap[p] = heap[p], heap[i]
        p = i
        i = get_children(p)

def extract_min():
    r = heap.pop(0) # deleting root
    if len(heap) == 0:
        return r
    heap.insert(0, heap.pop(-1)) # move last leaf to be new root
    bubble_down()
    return r

if __name__ == "__main__":
    data = []
    with open("data.txt", "r") as file:
        for line in file:
            l = line.strip().split()
            edges = []
            for edge in l[1:]:
                edges.append(tuple([int(x) for x in edge.split(",")]))
            data.append([int(l[0])] + edges)
    for e in data[0][1:]:
        insert(e)
    print(heap)