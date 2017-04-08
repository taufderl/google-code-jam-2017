#!/usr/bin/env python3

import sys

def get_LR(B):
  L = [None] * len(B)
  for i in range(len(B)):
    if B[i]:
      L[i] = -1 # occupied
    else:
      L[i] = L[i-1]+1
  R = [None]*len(B)
  for i in reversed(range(len(B))):
    if B[i]:
      R[i] = -1
    else:
      R[i] = R[i+1]+1
  return L, R


def new_user(B):
  L, R = get_LR(B)
  MIN = [min(L[i], R[i]) for i in range(len(B))]
  MAX = [max(L[i], R[i]) for i in range(len(B))]
  COMBO = [(MIN[i], MAX[i]) for i in range(len(B))]
  c = max(COMBO)
  y, x = c
  index = COMBO.index(c)
  """
  print('B  ', B)
  print('L  ', L)
  print('R  ', R)
  print('MIN', MIN)
  print('MAX', MAX)
  print('COMBO', COMBO)
  print(max(COMBO), COMBO.index(max(COMBO)))
  print(10*'-')
  """
  return index, x, y


def calculate(data):
  data = data.split(' ')
  N, K = int(data[0]), int(data[1])
  B = [True] + N*[False] + [True]
  for i in range(K):
    index, x, y = new_user(B)
    #print(index, x, y)
    B[index] = True
  return "{} {}".format(x, y)
  

def process_file(filename):
  data = []
  with open(filename, 'r') as infile:
    data = infile.readlines()
  count, data = int(data[0]), [x.strip() for x in data]
  i = 1
  while i <= count:
    print("Case #{}: {}".format(i, calculate(data[i])))
    print("Case #{}: {}".format(i, calculate(data[i])), file=sys.stderr)
    i += 1


def main():
  filename = 'C-my.in'
  filename = 'C-small-1-attempt0.in'
  #filename = 'C-small-1-attempt1.in'
  #filename = 'C-small-1-attempt2.in'
  #filename = 'C-small-2-attempt0.in'
  #filename = 'C-large.in'
  process_file(filename)


if __name__ == '__main__':
  main()
