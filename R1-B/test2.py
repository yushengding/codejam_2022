
testcases = input()




def solve(line):
  N, P = [int(s) for s in input().strip().split(' ')]
  
  Xss = [[int(s) for s in input().strip().split(' ')] for i in range(N)]
  X2s = [[min(Xs), max(Xs)] for Xs in Xss]

  ans = [(0, 0), (0 ,0)] # start 0 with 0 press, start 0 with 0 press
  for x0, x1 in X2s:
    y00, y01 = ans[0]
    y10, y11 = ans[1]
    ny00 = x0
    ny01 = min(abs(y00 - x1) + y01, abs(y10 - x1) + y11) + x1 - x0
    ny10 = x1
    ny11 = min(abs(y00 - x0) + y01, abs(y10 - x0) + y11) + x1 - x0
    ans = [(ny00, ny01), (ny10, ny11)]
  return min(ans[0][1], ans[1][1])


for caseNr in range(1, int(testcases) + 1):
    print("Case #%i: %s" % (caseNr, solve(caseNr)))


