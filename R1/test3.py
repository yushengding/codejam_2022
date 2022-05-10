from itertools import permutations
testcases = input()

def solve(E, W):
  last_layer = {(): 0}
  next_layer = {(): 0}
  for i in range(E):
    ws = map(int, input().strip().split(' '))
    new_layer = ''
    for c, w in zip(['A', 'B', 'C'], ws):
      new_layer + c*w
    for p in permutations(new_layer):
      for i in range(len(p)):
        if p[:i] in last_layer:
          next_layer[p] = min(next_layer[p], last_layer[p[:i]] + len(p) - i)
    

  for c in line.strip():
    if s and s[-1][0] == c:
      s[-1][1] += 1
    else:
      s.append([c, 1])
  ans = ''
  for (c0, count0), (c1, count1) in zip(s, s[1:]):
    if c0 < c1:
      ans += c0 * (count0 * 2)
    else:
      ans += c0 * count0
  ans += s[-1][0] * s[-1][1]

  return ans


for caseNr in range(1, int(testcases) + 1):
    E, W = map(int, input().strip().split(' '))
    print("Case #%i: %s" % (caseNr, solve(E, W)))


