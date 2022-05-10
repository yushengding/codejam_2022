import enum
import sys
from collections import defaultdict
sys.setrecursionlimit(100010)
from functools import lru_cache
def output(string):
  print(string)
  sys.stdout.flush()

def read(f=lambda x: x, split=' '):
  return [f(s) for s in input().strip().split(split)]

testcases, = read(int)

mod = int(1e9+7)
@lru_cache(None)
def getP(A):
  if A == 1:
    return 1
  else:
    return A * getP(A-1) % mod
for i in range(1, int(1e5)):
  getP(i)

def getD(v, m):
    ans = 1
    while m:
      if m & 1 == 1:
        ans *= v
        ans %= mod
      v *= v
      v %= mod
      m //= 2
    return ans

def getC(all, min):
  if min == 0 or min == all:
    return 1
  return getP(all) * getD(getP(min) * getP(all - min) % mod, mod - 2) % mod

def solve(T):
  N, = read(int)
  Vs = read(int)
  waitlist = []
  edges = set()
  for i, v in enumerate(Vs):
    top = None
    if v > 1 + len(waitlist):
      return 0
    while len(waitlist) >= v:
      top = waitlist.pop()
    if top and waitlist:
      edges.remove((waitlist[-1], top))
    edges.add((waitlist[-1], i))
    edges.add((i, top))
  graph = defaultdict(list)
  for i, j in edges:
    graph[i].append(j)
  
  def helper(i, N):
    ans = 1
    for child in graph[i]:
      



  



for caseNr in range(1, int(testcases) + 1):
    print("Case #%i: %s" % (caseNr, solve(caseNr)))


