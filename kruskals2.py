# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
from dataclasses import dataclass
import random
import time as tm
import numpy as np
from collections import defaultdict

rows, cols = (5, 5)
graph = np.zeros([rows,cols],int)
#-----------------------------------------------------------------------------------------------------------------
@dataclass
class Node:
    wt: int
    fro : int
    to : int
#-----------------------------------------------------------------------------------------------------------------
array = [Node(0,0,0)]
array.clear()
result = [Node(0,0,0)]
result.clear()
#-----------------------------------------------------------------------------------------------------------------
def GraphGenerate():
    for i in range (0,rows):
        for j in range(i+1,cols):
            graph[i][j] = random.randint(1,10)
            if(graph[i][j]!=0):
                array.append(Node(graph[i][j],i,j))
            graph[j][i] = graph[i][j]
#-----------------------------------------------------------------------------------------------------------------
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i].wt < arr[l].wt:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest].wt < arr[r].wt:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

 #-----------------------------------------------------------------------------------------------------------------

# Driver code to test above
GraphGenerate()
# for i in range(len(array)):
    # print(array[i])
print("############################")
heapSort(array)
# for i in range(len(array)):
    # print(array[i])
while(len(result) <= rows-1){

}
