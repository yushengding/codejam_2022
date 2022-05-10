testcases = input()


def solve():
  init = [int(1e6)] * 4

  for i in range(3):
    new_machine = map(int, input().strip().split(" "))
    init = list(map(min, zip(init, new_machine)))
  if sum(init) >= int(1e6):
    ans = []
    total = 0
    for i in init:
      if i + total >= int(1e6):
        ans.append(int(1e6) - total)
        total = int(1e6)
      else:
        ans.append(i)
        total += i
    return ' '.join(map(str, ans))
  
  return 'IMPOSSIBLE'



for caseNr in range(1, int(testcases) + 1):
    
    print("Case #%i: %s" % (caseNr, solve()))

