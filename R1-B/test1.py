
testcases = input()

def solve(line):
  n = int(input().strip())
  ds = [int(s) for s in input().strip().split(' ')]
  ans = []
  l = 0
  r = len(ds) - 1
  while l <= r:
    if ds [l] < ds[r]:
      ans.append(ds[l])
      l += 1
    else:
      ans.append(ds[r])
      r -= 1

  last = 0
  res = 0
  # print(ans)
  for i in ans:
    if i >= last:
      res += 1
      last = i
  return res

for caseNr in range(1, int(testcases) + 1):
    print("Case #%i: %s" % (caseNr, solve(caseNr)))


