def isCyclic(g,n):
    # g - Adjacency list of graph / n - no. of vertices
    if bfs(g):
        return "No cycle\n"
    else:
        return "Cycle is present\n"

def bfs(graph):
    explored = []
    isBackEdge = True
    vertexList = list(graph.keys())
    for i in vertexList:
        queue = [i]
        while queue:
            node = queue.pop(0)
            if node not in explored:
                explored.append(node)
                vertexList.remove(node)
                neighbours = graph[node]
                for neighbour in neighbours:
                    if neighbour not in explored:
                        queue.append(neighbour)
            else:
                isBackEdge = False
                break
    return isBackEdge
 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import io
import sys
from collections import defaultdict


#Graph Class:
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)

if __name__ == '__main__':
    test_cases = int(input("No. of test cases: "))
    for cases in range(test_cases) :
        N,E = map(int,input("|V| |E|: ").strip().split())
        g = Graph(N)
        edges = list(map(int,input("Edges: ").strip().split()))

        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            g.addEdge(u,v) # add an undirected edge from u to v
            g.addEdge(v,u)
        print(isCyclic(g.graph,N))
# } Driver Code Ends