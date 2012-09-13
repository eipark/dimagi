#!/usr/bin/env python

##### 3) Number Counting #####

# simple brute force solution
# O(n)
def numberCounter(n):
  count = 0
  if n > 1 and isinstance(n, int):
    for num in range(1, n+1):
      if '7' not in str(num):
        count += 1
  else:
    print n + " is not a valid input. Must be integer greater than 1"

  print count
  return count

#numberCounter(800)
#numberCounter(700)
numberCounter(70)
numberCounter(3)
#numberCounter(773)
##1, 2, 3, 4, 5, 6, 7, 8
