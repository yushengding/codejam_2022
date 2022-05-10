import sys
def output(string):
  print(string)
  sys.stdout.flush()


testcases, N = [int(s) for s in input().strip().split(' ')]

def solve(T):
  for i in range(N-1):
    output(f'M {i+1} {N}')
    min_index = int(input().strip())
    if i + 1 != min_index:
      output(f'S {i+1} {min_index}')
      int(input().strip())
  output('D')
  int(input().strip())
for caseNr in range(1, int(testcases) + 1):
    solve(caseNr)


