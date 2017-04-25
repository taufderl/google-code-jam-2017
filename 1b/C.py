#!/usr/bin/env python3

import sys
from sortedcontainers import SortedDict

def eprint(x):
  print(x, file=sys.stderr)


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
  #filename = 'C-small-attempt0.in'
  #filename = 'C-large.in'
  process_file(filename)


if __name__ == '__main__':
  main()
