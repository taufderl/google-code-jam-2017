#!/usr/bin/env python3

import sys
from sortedcontainers import SortedDict

def eprint(x):
  print(x, file=sys.stderr)

# new concept
def calculate3(data):
  data = data.split(' ')
  N, K = int(data[0]), int(data[1])
  if N == K:
    return "0 0"
  k = K
  B = SortedDict()
  B[N] = 1
  while k > 0:
    m, n = B.popitem()
    k -= n
    if m%2 == 0:
      g1, g2 = int(m/2)-1, int(m/2)
    else:
      g1, g2 = int(m/2), int(m/2)
    B[g1] = B[g1] + n if g1 in B else n
    B[g2] = B[g2] + n if g2 in B else n
  return "{} {}".format(g2, g1)


def process_file(filename):
  data = []
  with open(filename, 'r') as infile:
    data = infile.readlines()
  count, data = int(data[0]), [x.strip() for x in data]
  i = 1
  while i <= count:
    #eprint(data[i])
    result = calculate3(data[i])
    print("Case #{}: {}".format(i, result))
    eprint("Case #{}: {}".format(i, result))
    i += 1


def main():
  filename = 'C-my.in'
  filename = 'C-small-1-attempt0.in'
  filename = 'C-small-1-attempt1.in'
  filename = 'C-small-1-attempt2.in'
  filename = 'C-small-2-attempt0.in'
  filename = 'C-small-2-attempt1.in'
  filename = 'C-large.in'
  process_file(filename)


if __name__ == '__main__':
  main()
