#!/usr/bin/env python3

import sys
from sortedcontainers import SortedDict
import math
import operator
import functools
import heapq


def eprint(x):
  print(x, file=sys.stderr)

def calculate(N, K, U, cores):
  eprint(">>> {}=={} {} {}".format(N,K,U,cores.items()))
  while U:
    eprint("{} {} {}".format(N,U,cores.items()))
    # find lowest cores
    min_value, core_count = cores.popitem()
    eprint("Found lowest {}".format(min_value))
    if not cores:
      # if no cores left., spread this and break
      new_value = min_value-(U/core_count)
      U = 0
      cores[new_value] = core_count
      break
    next_min = max(list(cores))
    eprint("NEXT MIN {}".format(next_min))
    diff = min_value-next_min
    eprint("DIFF {}".format(diff))
    if U>core_count*diff:
      # spread all the U
      U -= core_count*diff
      cores[next_min] += core_count
    else:
      # We don't have enough U to spread, spread the lasting
      new_value = min_value-(U/core_count)
      U = 0
      cores[new_value] = core_count
      break
  eprint("{} {} {}".format(N,U,cores.items()))
  r = functools.reduce(operator.mul, [x**y for x,y in cores.items()], 1)
  r = math.fabs(r)
  r = str(r)
  if 'e' in r:
    r = '0.0'
  if r.startswith('1.0'):
    r = '1.0'
  return r
  
def process_file(filename):
  data = []
  with open(filename, 'r') as infile:
    data = infile.readlines()
  count, data = int(data[0]), [x.strip() for x in data[1:]]
  eprint(count)
  cases = []
  for i in range(count):
    x = data.pop(0).split(' ')
    N, K = int(x[0]), int(x[1])
    x = data.pop(0).split(' ')
    U = float(x[0])
    x = data.pop(0).split(' ')
    P = [float(a) for a in x]
    cores = SortedDict()
    for p in P:
      if p in cores:
        cores[-p] += 1
      else:
        cores[-p] = 1
    cases.append((N,K,U, cores))

  i = 1
  for N, K, U, cores in cases:
    result = calculate(N,K,U,cores)
    print("Case #{}: {}".format(i, result))
    eprint("Case #{}: {}".format(i, result))
    i += 1

def main():
  filename = 'C-my.in'
  filename = 'C-small-1-attempt0.in'
  #filename = 'C-small-1-attempt1.in'
  #filename = 'C-small-1-attempt2.in'
  filename = 'C-small-1-attempt3.in'
  filename = 'C-small-practice-1.in'
  process_file(filename)


if __name__ == '__main__':
  main()
