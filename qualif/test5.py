from collections import defaultdict
import sys
import random
from tabnanny import check
def MySolution():
  N, K = list(map(int, input().strip().split(" ")))
  start_room, pass_num = list(map(int, input().strip().split(" ")))
  checked = set([start_room])
  if N <= K:
    for new_cave in random.sample(range(1,N+1), k=min(N, K)):
      print('T {}'.format(new_cave))
      sys.stdout.flush()
      n_start_room, n_pass_num = list(map(int, input().strip().split(" ")))
      pass_num += n_pass_num
    print('E {}'.format(int(pass_num * N / min(N, K) // 2 )))
    sys.stdout.flush()
  else:
    count = K
    sample = {}
    known = {}
    while count > 2:
      for new_cave in random.sample(range(1,N+1), k=1):
        
        if new_cave not in checked:  
          count -= 1
          checked.add(new_cave)  

          print('T {}'.format(new_cave))
          sys.stdout.flush()
          n_start_room, n_pass_num = list(map(int, input().strip().split(" ")))
          pass_num += n_pass_num
          sample[n_start_room] = n_pass_num 
          if count > 7000:
            count -= 1
            print('W')
            sys.stdout.flush()
            n_start_room, n_pass_num = list(map(int, input().strip().split(" ")))
            if n_start_room not in checked:
              checked.add(n_start_room)
              # pass_num += n_pass_num
              known[n_start_room] = n_pass_num
    
    for i in known:
      if i in sample:
        del sample[i]

    ans = sum(sample.values()) / len(sample) * (N - len(known)) / 2 + sum(known.values()) / 2

    print('E {}'.format(int(ans)))
    sys.stdout.flush()



  return   
  
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  MySolution()