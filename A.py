#!/usr/bin/env python3

import sys
import re

sys.setrecursionlimit(1500)

done_case = re.compile(r'^\++$')

def flip(S, i, K):
  a = list(S)
  for x in range(i, i+K):
    a[x] = '+' if a[x] == '-' else '-'
  Snew = ''.join(a)
  #print(i, K, S, Snew)
  return Snew

def shortest(S, K):
  if done_case.match(S):
    return 0
  i = S.index('-')
  if i+K > len(S):
    return 'IMPOSSIBLE'
  else:
    x = shortest(flip(S, i, K), K)
    if x == 'IMPOSSIBLE':
      return 'IMPOSSIBLE'
    else:
      return 1 + x

def calculate(data):
  data = data.split(' ')
  S, K = data[0], int(data[1])
  x = shortest(S, K)
  return str(x)
  

def process_file(filename):
  data = []
  with open(filename, 'r') as infile:
    data = infile.readlines()
  count, data = int(data[0]), [x.strip() for x in data]
  i = 1
  while i <= count:
    print("Case #{}: {}".format(i, calculate(data[i])))
    i += 1


def main():
  #filename = 'A-my.in'
  #filename = 'A-small-attempt0.in'
  filename = 'A-large.in'
  process_file(filename)


if __name__ == '__main__':
  main()
