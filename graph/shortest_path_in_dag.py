# Given a Directed Acyclic Graph of N vertices from 0 to N-1 and M edges and a 2D Integer array edges, where there is a directed edge from vertex edge[i][0] to vertex edge[i][1] with a distance of edge[i][2] for all i.
# Find the shortest path from source vertex to all the vertices and if it is impossible to reach any vertex, then return -1 for that vertex. The source vertex is assumed to be 0.
class Solution:
  def dfs(self,node,adj,visited,stack):
    visited[node] = True
    for child,weight in adj[node]:
      if not visited[child]:
        self.dfs(child,adj,visited,stack)

    stack.append(node)
  
  def shortestPath(self, N, M, edges):
    adj = [[] for _ in range(N) ]

    for i in range(M):
      edge = edges[i]
      adj[edge[0]].append((edge[1],edge[2]))  

    stack = []
    visited = [False]*N
    for i in range(N):
      if not visited[i]:
        self.dfs(i,adj,visited,stack)

    distance = [float('inf')] * N
    source = 0
    distance[source] = 0

    while len(stack) != 0:
      node = stack.pop()
      dist = distance[node]
      for adjNode,weight in adj[node]:
        if weight + dist < distance[adjNode]: 
          distance[adjNode] = weight + dist

    for index,value in enumerate(distance):
      if distance[index] == float('inf'):
        distance[index] = -1
    return distance

if __name__ == "__main__":
  N = 4
  M = 2 
  edges = [[0,1,2],[0,2,1]]
  print(Solution().shortestPath(N,M,edges))