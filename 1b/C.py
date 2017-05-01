#!/usr/bin/env python3

import sys
from collections import OrderedDict
from sortedcontainers import SortedDict

def eprint(x):
  print(x, file=sys.stderr)


def calculate(N, Q, horses, cities, routes):
  print(N, Q, horses, cities, routes)
  for _from, _to in routes:
    E, S = horses[_from-1]
    
  times = []
  return 0


def process_file(filename):
  data = []
  with open(filename, 'r') as infile:
    data = infile.readlines()
  count, data = int(data[0]), [x.strip() for x in data[1:]]
  cases = []
  eprint(count)
  for T in range(count):
    x = data.pop(0).split(' ')
    N, Q = int(x[0]), int(x[1])
    horses = {}
    for i in range(1, N+1):
      x = data.pop(0).split(' ')
      Ei, Si = int(x[0]), int(x[1])
      horses[i] = (Ei, Si)
    cities = {}
    for i in range(1, N+1):
      x = data.pop(0).split(' ')
      x = [(index+1,int(var)) for index, var in enumerate(x)]
      cities[i] = dict(x)
    routes = []
    for i in range(Q):
      x = data.pop(0).split(' ')
      Uk, Vk = int(x[0]), int(x[1])
      routes.append((Uk, Vk))
      
    eprint(cities)
    cases.append((N, Q, horses, cities, routes))
  eprint(len(cases))

  i = 1
  for N, Q, horses, cities, routes in cases:
    #eprint(data[i])
    result = calculate(N, Q, horses, cities, routes)
    print("Case #{}: {}".format(i, result))
    eprint("Case #{}: {}".format(i, result))
    i += 1


def main():
  filename = 'C-my.in'
  #filename = 'C-small-attempt0.in'
  #filename = 'C-large.in'
  process_file(filename)


if __name__ == '__main__':
  main()
