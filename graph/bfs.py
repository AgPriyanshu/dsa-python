from collections import deque

def bfs(V,adj):
  queue = deque()
  visited = {}
  queue.append(0)
  for i in range(V):
    for node in adj[i]:
      if visited.get(node):
        continue
      else:
        queue.append(node)
        visited[node] = True
  
  while len(queue) > 0:
    print(queue.popleft(),end=" ")

if __name__ == "__main__":
  adj = [[2,3,1],[0],[0,4],[0],[2]]
  V = 5
  bfs(5,adj)
