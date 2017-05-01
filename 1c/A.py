#!/usr/bin/env python3

import sys
from sortedcontainers import SortedDict
import math
from itertools import combinations

def eprint(x):
  print(x, file=sys.stderr)

def F(p):
  R, h = p
  return math.pi * R * R

def H(p):
  R, h = p
  return 2 * math.pi * R * h


def surface(pancakes):
  return sum([H(p) for p in pancakes]) + max([F(p) for p in pancakes])

def calculate3(N,K,pancakes):
  if N == K:
    return surface(pancakes)
  elif K == 1:
    return max([surface([x]) for x in pancakes])
  else:
    # start with biggest and iterate
    chosen = []
    surfaces = [surface([p]) for p in pancakes]
    m = max(surfaces)
    i = surfaces.index(m)
    chosen.append(pancakes[i])
    del pancakes[i]
    while len(chosen) < K:
      surfaces = [surface(chosen + [p]) for p in pancakes]
      m = max(surfaces)
      i = surfaces.index(m)
      chosen.append(pancakes[i])
      del pancakes[i]
  return m


def calculate2(N,K,pancakes):
  if N == K:
    return surface(pancakes)
  elif K == 1:
    return max([surface([x]) for x in pancakes])
  else:
    combis = combinations(pancakes, K)
    return max([surface(c) for c in combis])

def calculate(N, K, pancakes):
  A = []
  for p in pancakes:
    A.append(F(p)+H(p))
  chosen = []
  for i in range(K):
    m = max(A)
    i = A.index(m)
    # choose pancake i with A=m
    eprint("Choose {} with {}".format(pancakes[i],m))
    chosen.append(pancakes[i])
    A[i] = -1

  #print(N, K, chosen)
  syrup = sum([H(p) for p in chosen])
  # add F
  syrup2 = max([F(p) for p in chosen])
  return syrup + syrup2

  
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
    pancakes = []
    for j in range(N):
      x = data.pop(0).split(' ')
      R, H = int(x[0]), int(x[1])
      pancakes.append((R,H))
    cases.append((N,K,pancakes))

  i = 1
  for N, K, p in cases:
    result = calculate3(N,K,p)
    print("Case #{}: {}".format(i, result))
    eprint("Case #{}: {}".format(i, result))
    i += 1

def main():
  filename = 'A-my.in'
  filename = 'A-small-attempt0.in'
  filename = 'A-small-attempt1.in'
  filename = 'A-large.in'
  filename = 'A-large-practice.in'
  process_file(filename)


if __name__ == '__main__':
  main()
