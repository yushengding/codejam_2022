import sys
import random
testcases = input()

def output(v, log=None):
  # log.write("output {}\n".format(v))
  print(v)
  sys.stdout.flush()
def do_try():
  log = None

  output("10101010", log)
  N = int(input().strip())
  if N != 4:
    return N

  output("10101010", log)
  N = int(input().strip())
  if N != 4:
    return N

  output("11001100", log)
  N = int(input().strip())
  if N != 4:
    return N

  output("10101010", log)
  
  N = int(input().strip())
  if N != 4:
    return N

  output("10101010", log)
  N = int(input().strip())
  if N != 4:
    return N
  return N

def solve(line):
  log = None
  output("11111111", log)
  N = int(input().strip())
  # log.write("{}\n".format(N))
  while N != 0:
    if N == 8:
      output("11111111", log)
    if N == 4:
      N = do_try()
      continue
    else:
      s = [random.randint(0, 7) for i in range(N)]
      output("".join(['1' if i in s else '0' for i in range(8) ]), log)
    
    N = int(input().strip())

for caseNr in range(1, int(testcases) + 1):
  solve(0)

