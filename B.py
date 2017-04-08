#!/usr/bin/env python3

import sys

def is_tidy(number):
  s = str(number)
  for i in range(1, len(s)):
    if s[i] < s[i-1]:
      return False
  return True


def nextnumber(number):
  s = str(number)
  last_increase = 0
  for i in range(0, len(s)-1):
    #print(s[i], s[i+1])
    if s[i] < s[i+1]:
      last_increase = i+1
    elif s[i] > s[i+1]:
      break
  #print(s)
  #print(' '*last_increase + '^')
  s = list(s)
  s[last_increase] = str(int(s[last_increase]) - 1)
  for i in range(last_increase+1, len(s)):
    s[i] = '9'
  return int(''.join(s))
    
      


def calculate(number):
  i = number
  while i>0:
    #print(i)
    if is_tidy(i):
      return i
    else:
      i = nextnumber(i)
  # TODO here is room to do the work
  return i
  

def process_file(filename):
  data = []
  with open(filename, 'r') as infile:
    data = infile.readlines()
  count, data = int(data[0]), [int(x) for x in data]
  i = 1
  while i <= count:
    print("Case #{}: {}".format(i, calculate(data[i])))
    i += 1


def main():
  filename = 'B-my.in'
  filename = 'B-small-attempt0.in'
  filename = 'B-large.in'
  process_file(filename)


if __name__ == '__main__':
  main()
