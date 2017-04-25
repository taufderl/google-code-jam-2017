#!/usr/bin/env python3

import sys
from collections import OrderedDict
from sortedcontainers import SortedDict

def eprint(x):
  print(x, file=sys.stderr)


def calculate(D, horses):
  times = []
  for Ki, Si in horses:
    time = (D-Ki)/Si
    times.append(time)
  maxtime = max(times)
  return D/maxtime


def process_file(filename):
  data = []
  with open(filename, 'r') as infile:
    data = infile.readlines()
  count, data = int(data[0]), [x.strip() for x in data[1:]]
  cases = []
  eprint(count)
  for i in range(count):
    x = data.pop(0).split(' ')
    D, N = int(x[0]), int(x[1])
    horses = []
    K = []
    for j in range(N):
      x = data.pop(0).split(' ')
      Ki, Si = int(x[0]), int(x[1])
      horses.append((int(Ki), int(Si)))
    eprint("{} {} {}".format(D, N, horses))
    cases.append((D, horses))
  eprint(len(cases))

  i = 1
  for D, horses in cases:
    #eprint(data[i])
    result = calculate(D, horses)
    print("Case #{}: {}".format(i, result))
    eprint("Case #{}: {}".format(i, result))
    i += 1


def main():
  filename = 'A-my.in'
  filename = 'A-small-attempt0.in'
  filename = 'A-small-attempt1.in'
  filename = 'A-large.in'
  process_file(filename)


if __name__ == '__main__':
  main()
