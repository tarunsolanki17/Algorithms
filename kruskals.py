import heapq
import random
import time as tm
import numpy as np
from collections import defaultdict
import sys


rows, cols = (5, 5)
graph = np.zeros([rows,cols],int)
arr_nx3 = [[0]*3]*1
#--------------------------------------------------------------------------------------------#
def GraphGenerate():

    arr_nx3.clear()
    # print(arr_nx3)
    for i in range (0,rows):
        for j in range(i+1,cols):
            graph[i][j] = random.randint(0,10)
            if(graph[i][j]!=0):
                arr_nx3.append([graph[i][j],i,j])
            graph[j][i] = graph[i][j]


    # print(graph)
    # print(arr_nx3)
#--------------------------------------------------------------------------------------------#
def heapify(arr, n, i,col_index):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i][0] > arr[l][0]:
        smallest = l

    if r < n and arr[smallest][0] > arr[r][0]:
        smallest = r

    if smallest != i:
        temp = arr[smallest]
        arr[smallest] = arr[i]
        arr[i] = temp

        heapify(arr, n, smallest,col_index)

#-----------------------------------------------------------------------------------------------------
def heapSort(arr):
    col_index=0
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i,col_index)

def deleteMin(arr):
    heapify(arr,len(arr),0,0)
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i][0], arr[0][0] = arr[0][0], arr[i][0]   # swap
        heapify(arr, i, 0,0)

#-----------------------------------------------------------------------------------------------------
# def cycleCheck(MST):
class Graph:

    def __init__(self, num_of_v):
        self.num_of_v = num_of_v
        self.edges = defaultdict(list)

    # graph is represented as an
    # array of edges
    def add_edge(self, u, v):
        self.edges[u].append(v)

    def removeEdge(self,u,v):
        self.edges[u].remove(v)


class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

# A utility function to find set of an element
# node(uses path compression technique)
def find(subsets, node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets, subsets[node].parent)
    return subsets[node].parent

# A function that does union of two sets
# of u and v(uses union by rank)
def union(subsets, u, v):

    # Attach smaller rank tree under root
    # of high rank tree(Union by Rank)
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent = v

    # If ranks are same, then make one as
    # root and increment its rank by one
    else:
        subsets[v].parent = u
        subsets[u].rank += 1

# The main function to check whether a given
# graph contains cycle or not
def isCycle(graph):

    # Allocate memory for creating sets
    subsets = []

    for u in range(graph.num_of_v):
        subsets.append(Subset(u, 0))

    # Iterate through all edges of graph,
    # find sets of both vertices of every
    # edge, if sets are same, then there
    # is cycle in graph.
    for u in graph.edges:
        u_rep = find(subsets, u)

        for v in graph.edges[u]:
            v_rep = find(subsets, v)

            if u_rep == v_rep:
                return True
            else:
                union(subsets, u_rep, v_rep)
#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------
# print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
tic = tm.perf_counter()

GraphGenerate()
heapSort(arr_nx3)
arr2 = arr_nx3[0:][0]
# print(arr_nx3)

MST = [[0]*3]*1
MST.clear()
g = Graph(rows)
                        # ||len(arr_nx3)>0
while((len(MST)<=rows-1) and (len(arr_nx3)>0)):

    # temp_graph = g
    # temp_graph.addEdge(arr_nx3[0][1],arr_nx3[0][2])
    g.add_edge(arr_nx3[0][1],arr_nx3[0][2])
    val = len(arr_nx3)-1
    if isCycle(g):
        g.removeEdge(arr_nx3[0][1],arr_nx3[0][2])

        arr_nx3[0][0] = arr_nx3[val][0]
        arr_nx3[0][1] = arr_nx3[val][1]
        arr_nx3[0][2] = arr_nx3[val][2]
        arr_nx3.pop(len(arr_nx3)-1)
        deleteMin(arr_nx3)
        # arr_nx3.pop(0)
        # heapSort(arr_nx3)
        continue
    else:
        # print("Run2")
        MST.append([arr_nx3[0][0],arr_nx3[0][1],arr_nx3[0][2]])
        arr_nx3[0][0] = arr_nx3[val][0]
        arr_nx3[0][1] = arr_nx3[val][1]
        arr_nx3[0][2] = arr_nx3[val][2]
        arr_nx3.pop(len(arr_nx3)-1)
        deleteMin(arr_nx3)
        # arr_nx3.pop(0)
        # heapSort(arr_nx3)


print((MST))














toc = tm.perf_counter()
print("Time = ",toc-tic)
