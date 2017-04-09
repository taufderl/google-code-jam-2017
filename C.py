#!/usr/bin/env python3

import sys

def eprint(x):
  print(x, file=sys.stderr)


def calculate2(data):
  data = data.split(' ')
  N, K = int(data[0]), int(data[1])
  if N == K:
    return "0 0"
  # initialize LR and priolist
  L = [-1] + list(range(0, N)) + [-1]
  R = [-1] + list(range(N-1, 0-1, -1)) + [-1]
  MINMAX = [(min(L[i],R[i]), max(L[i],R[i])) for i in range(len(L))]
  assert(len(L) == len(R))
  for i in range(K):
    #eprint("*********ITERATION " + str(i) + " ITERATION*********")
    #eprint('L  ', L)
    #eprint('R  ', R)
    #eprint('MINMAX', MINMAX)
    #eprint(10*'-')
    c = max(MINMAX)
    #eprint(c)
    y, x = c
    new_user = MINMAX.index(c)
    #eprint(new_user)
    eprint("%i %s"%(new_user, str(c)))
    L[new_user] = -1
    R[new_user] = -1
    MINMAX[new_user] = (-1, -1)
    # update all in L from new_user til next found user
    eprint("                     START: "+str(new_user+1))
    for i in range(new_user+1, len(L)):
      if L[i] == -1: # found next user, break
        eprint("                       END: "+str(i))
        break
      else:
        L[i] = L[i-1]+1
        #eprint("OLD     %s"%str(MINMAX[i]))
        MINMAX[i] = (min(L[i],R[i]), max(L[i],R[i]))
        #eprint("UPDATED %s"%str(MINMAX[i]))
    # update all in R from new_user towards the left
    for i in range(new_user-1, 0-1, -1):
      if R[i] == -1:
        break
      else:
        R[i] = R[i+1]+1
        MINMAX[i] = (min(L[i],R[i]), max(L[i],R[i]))
    #eprint('MINMAX', MINMAX)
  return "{} {}".format(x, y)


# new concept
def calculate3(data):
  data = data.split(' ')
  N, K = int(data[0]), int(data[1])
  if N == K:
    return "0 0"
  B = [N]
  for k in range(K):
    m = max(B) # find biggest gap
    i = B.index(m) # find first occurence of gap
            # split gap
    if m%2 == 0:
      g1, g2 = int(m/2)-1, int(m/2)
    else:
      g1, g2 = int(m/2), int(m/2) # notice, we are 'losing' 1 here
    B[i] = g2
    B.insert(i, g1)
    eprint("%i %i"%(K, len(B)))
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
  #filename = 'C-large.in'
  process_file(filename)


if __name__ == '__main__':
  main()
