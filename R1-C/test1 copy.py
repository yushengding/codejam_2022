
testcases = input()

def solve(line):
  n = int(input().strip())
  
  words = list(input().strip().split(" "))
  ll = sum(len(w) for w in words)
  pure = [s for s in words if len(set(s)) == 1]
  others = [s for s in words if len(set(s)) > 1]
  words = pure + others
  others = ''
  for i in range(len(words)):
    
    for j in range(i+1, len(words)):
      if words[j][0] == words[i][-1]:
        words[j] = words[i] + words[j]
        break
      elif words[j][-1] == words[i][0]:
        words[j] = words[j] + words[i]
        break
    else:
      others += words[i]
  ans = others
  if len(ans) == ll:
    finished = set()
    last = ''
    for i in range(len(ans)):
      if ans[i] in finished:
        return "IMPOSSIBLE"
      elif ans[i] != last:
        finished.add(last)
        last = ans[i]
    return ans
  else:
    return "IMPOSSIBLE"
      

for caseNr in range(1, int(testcases) + 1):
    print("Case #%i: %s" % (caseNr, solve(caseNr)))


