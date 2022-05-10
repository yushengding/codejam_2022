from collections import defaultdict
import sys
print(sys.setrecursionlimit(100001))
class MyNode():
  def __init__(self, fun=0):
    self.fun = fun
    self.children = []
  def add_child(self, child_node):
    self.children.append(child_node)
    
def MySolution():
  n = int(input())
  Fs = list(map(int, input().strip().split(" ")))
  Ps = list(map(int, input().strip().split(" ")))
  nodes = {-1: MyNode(0)}
  
  for i in range(n):
    f = Fs[i]
    p = Ps[i]
    nodes[i] = MyNode(f)
    nodes[p-1].add_child(nodes[i])

  ans = [0]
  def helper(node, ans):
    if not node.children:
      return node.fun
    min_fun = None
    for child in node.children:
      v = helper(child, ans)
      if min_fun == None:
        min_fun = v
        continue
      elif min_fun <= v:
        ans[0] += v
      else:
        ans[0] += min_fun
        min_fun = v
    return max(min_fun, node.fun)

  s = helper(nodes[-1], ans)
  ans[0] += s
  return str(ans[0])


t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  print("Case #{}: {}".format(i, MySolution()))