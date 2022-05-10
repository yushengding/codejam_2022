testcases = input()

def solve():
  n = int(input())
  ss = list(map(int, input().strip().split(" ")))
  ss.sort()
  length = 0
  for i, s in enumerate(ss):
    if s > length:
      length += 1
    
  return s

for caseNr in range(1, int(testcases) + 1):
    print("Case #%i: %s" % (caseNr, solve()))

