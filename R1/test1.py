testcases = input()

def solve(line):
  s = []
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
    cipher = input()
    print("Case #%i: %s" % (caseNr, solve(cipher)))


