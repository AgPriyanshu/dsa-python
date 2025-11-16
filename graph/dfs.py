def dfs(node,adj,visited,ans):
  visited[node] = 1
  ans.append(node)
  for i in adj[node]:
    if visited[i] == 0:
      dfs(i,adj,visited,ans)

def dfsOfGraph( V, adj):
  visited,ans = [0]*V,[]
  dfs(0,adj,visited,ans)
  return ans

if __name__ == "__main__":
  adj = [[2,3,1],[0],[0,4],[0],[2]]
  V = 5
  print(dfsOfGraph(V,adj))