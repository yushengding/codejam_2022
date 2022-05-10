import random

T = 10
print(T)
for i in range(T):
  n = random.randint(1, 10)
  print(n)
  
  print(' '.join(map(str, [random.randint(1, int(10)) for i in range(n)])))
  
  print(' '.join(map(str, [random.randint(0, i) for i in range(n)])))
