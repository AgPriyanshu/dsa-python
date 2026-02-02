# Given a Directed Acyclic Graph of N vertices from 0 to N-1 and M edges and a 2D Integer array edges, where there is a directed edge from vertex edge[i][0] to vertex edge[i][1] with a distance of edge[i][2] for all i.
# Find the shortest path from source vertex to all the vertices and if it is impossible to reach any vertex, then return -1 for that vertex. The source vertex is assumed to be 0.
from collections import deque
class Solution:  
  def shortestPath(self, N, M, edges):
    adj = [[] for _ in range(N) ]

    for i in range(M):
      edge = edges[i]
      adj[edge[0]].append(edge[1])  

    distance = [float('inf')] * N
    source = 0
    distance[source] = 0

    q = deque()
    q.append((source,0))

    while q:
      node,node_dist = q.popleft()
      for child in adj[node]:
        if distance[child] == float('inf') or (node_dist + 1 < distance[child]):
          distance[child] = node_dist + 1
        q.append((child,distance[child]))
        

    for index,value in enumerate(distance):
      if distance[index] == float('inf'):
        distance[index] = '-1'
      else:
        distance[index] = str(distance[index])

    return " ".join(distance)

if __name__ == "__main__":
  n = 9
  m = 10
  edges = [[0,1],[0,3],[3,4],[4,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]]
  print(Solution().shortestPath(n,m,edges))