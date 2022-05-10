from multiprocessing.connection import wait
import sys
testcases = input()

def generate(i, start):
  return start, start + 97, start + 2**(i-1), start + 2**(i-1) + 97

def generate2(i, start):
  return start, start + i

def solve(N):
  # N is 100 of course
  s = set()
  diff_set = {}
  t = 0
  start = 5
  for i in range(1,12): # 36 nums to be able to create any diff in 2-1024
    while 2**i < 1e9:
      keys = generate(i, start) # A B C D :  (C+D) - (A+B) = 2^i
                                #            (A+D) - (B+C) = 0
      if all(c not in s for c in keys):
          diff_set[2**i] = keys
          s.update(keys)
          break
      start += 2

  for i in range(29, 1, -1): # 60 num to be create
    while 2**i < 1e9:
      keys = generate2(2**i, start) # A B: B - A = i
                                #      A - B = -1
      if all(c not in s for c in keys):
          diff_set[-2**i] = keys
          s.update(keys)
          break
      start += 2
# with open('testlog.log', 'w+') as outf:
  
  # outf.write('s here')
  # outf.write(str(list(map(str, s))))
  print(" ".join(map(str, s)))

  sys.stdout.flush()
  waitlist = sorted(list(map(int, input().strip().split(' '))))
  # outf.write('1 wat' + " ".join(str([len((waitlist))])))
  Aset = []
  Bset = []
  sA = 0
  sB = 0
  for A, B in zip(waitlist[::2], waitlist[1::2]):
    if sA > sB:
      A, B = B, A
    Aset.append(A)
    Bset.append(B)
    sA += A
    sB += B
  
  # outf.write('1 len A' + " ".join(str([len((Aset))])))
  # outf.write("\n")
  for k in sorted(diff_set.keys()):
    if k > 0:
      continue
    A, B = diff_set[k] # B > A
    if sA < sB:
      A, B = B, A
    Aset.append(A)
    Bset.append(B)
    sA += A
    sB += B
  if sA < sB:
    sA, sB = sB, sA
    Aset, Bset = Bset, Aset
  # outf.write(str(list(map(str, Aset))))
  # outf.write("\n")
  
  # outf.write('2 len A' + " ".join(str([len((Aset))])))
  # outf.write("\n")
  for k in sorted(diff_set.keys()):
    if k < 0:
      continue
    diff = sum(Aset) - sum(Bset)
    A, B, C, D = diff_set[k]    # A B C D :  (C+D) - (A+B) = 2^i
                                #            (A+D) - (B+C) = 0
    if diff & k > 0:
      Aset.append(A)
      Aset.append(B)
      Bset.append(C)
      Bset.append(D)
    else:
      Aset.append(A)
      Aset.append(D)
      Bset.append(C)
      Bset.append(B)
  
  # outf.write('3 len A' + " ".join(str([len((Aset))])))
  # outf.write(str(list(map(str, Aset))))
  # outf.write("\n")
  print(" ".join(map(str, Aset)))
  sys.stdout.flush()

    # outf.write(" ".join([str(sum(Aset)), str(sum(Bset))]))
    # outf.write("\n")
    # outf.write('len A' + " ".join(str([len((Aset))])))
    # outf.write("\n")
for caseNr in range(1, int(testcases) + 1):
    N = input()
    solve(N)
    # print("Case #%i: %s" % (caseNr, ))


