import sys
from functools import lru_cache
def output(string):
  print(string)
  sys.stdout.flush()

def read(f=lambda x: x, split=' '):
  return [f(s) for s in input().strip().split(split)]

testcases, = read(int)

def solve(T):
  N, = read(int)
  @lru_cache(None)
  def helper(n, begin=False):
    if n <= 1:
      return 0
    ans = 1
    for i in range(3 if begin else 2, 1 + int(n ** 0.5)):
      if n % i == 0:
        ans = max(ans, 1 + helper(n // i - 1, False))
        ans = max(ans, 1 + helper(i - 1, False))
    return ans

  return helper(N, True)

for caseNr in range(1, int(testcases) + 1):
    print("Case #%i: %s" % (caseNr, solve(caseNr)))


