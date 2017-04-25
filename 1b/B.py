#!/usr/bin/env python3

import sys
import operator
from sortedcontainers import SortedDict

"""
N, R, O, Y, G, B, and V.
"""
sys.setrecursionlimit(1500)

def eprint(x):
  print(x, file=sys.stderr)

def can_be_next(a, b):
  if a == b:
    return False
  if a == 'O' and b in ('R', 'Y'):
    return False
  if a == 'G' and b in ('Y', 'B'):
    return False
  if a == 'V' and b in ('R', 'B'):
    return False
  a,b = b,a
  if a == 'O' and b in ('R', 'Y'):
    return False
  if a == 'G' and b in ('Y', 'B'):
    return False
  if a == 'V' and b in ('R', 'B'):
    return False
  return True

def backtrack(N, out, types):
  if not types:
    if can_be_next(out[0], out[-1]):
      return out
    else:
      return 'IMPOSSIBLE'
  else:
    sorted_types = sorted(types.items(), key=operator.itemgetter(1), reverse=True)
    #eprint("{} {}".format(out, sorted_types))

    for unicorn, count in sorted_types:
      #eprint('Trying {} {}'.format(unicorn, sorted_types))
      if count and (not out or can_be_next(out[-1], unicorn)):
        new_types = types.copy()
        if count > 1: # add remaining, none if 0
          new_types[unicorn] = count - 1
        else:
          del new_types[unicorn]
        result = backtrack(N, out + unicorn, new_types)
        if not result == 'IMPOSSIBLE':
          return result
      else:
        pass
        #eprint("Couldn't place {} Have to try next".format(unicorn))
  return 'IMPOSSIBLE'
    

def place(data):
  types = {}
  N = data[0]
  if data[1]:
    types['R'] = data[1]
  if data[2]:
    types['O'] = data[2]
  if data[3]:
    types['Y'] = data[3]
  if data[4]:
    types['G'] = data[4]
  if data[5]:
    types['B'] = data[5]
  if data[6]:
    types['V'] = data[6]

  out = ''
  outlen = 0
  m = max(types.values())
  if m>N/2:
    return 'IMPOSSIBLE'
  return backtrack(N, out, types)


def process_file(filename):
  data = []
  with open(filename, 'r') as infile:
    data = infile.readlines()
  count, data = int(data[0]), [x.strip() for x in data]
  i = 1
  while i <= count:
    x = data[i].split(' ')
    x = [int(a) for a in x]
    #eprint(data[i])
    result = place(x)
    print("Case #{}: {}".format(i, result))
    eprint("Case #{}: {}".format(i, result))
    i += 1


def main():
  filename = 'B-my.in'
  #filename = 'B-small-attempt0.in'
  #filename = 'B-small-attempt1.in'
  #filename = 'B-small-attempt2.in'
  filename = 'B-large.in'
  filename = 'B-large-practice.in'
  process_file(filename)


if __name__ == '__main__':
  main()
