#!/usr/bin/env python

# Ernie Park, ernestipark@gmail.com, github.com/eipark, erniepark.com
##### 4) Dimagi Set Combination Challenge #####

'''
Based on spec given, I will assume the input is always properly formatted
as a list of lists with at least one list given.

Analysis: At first glance, I thought this was a very simple problem. I then realized
that it is more challenging because the depth (number of lists) is not fixed.
The basic mechanics of generating the combinations is simple and just requires nested
loops, but there was still the issue of the variable depth. I then thought a recursive
solution might make sense since you're performing the same action (looping) at every depth
except the final depth when you want to print the combination. The base case is when you're
at the max depth, and at each level, you call the looper function another level deeper
while maintaining a single array (print_list) of the current combination.

This solution is efficient in memory as you only have one main array (print_lists). Of course,
if we decided to return the solution instead of printing, it would take up as much memory as
there are combinations. I am assuming python is creating the smaller arrays I use by
reference and not by a copy, but I am not positive.
I'm not sure if you can make the solution much faster as we hit every combination
once - it would require a very clever trick to do so.
'''

def setCombo(word_lists):
  print_list = range(len(word_lists))
  looper(word_lists, print_list, 0)

def looper(word_lists, print_list, depth):
  curr_list = word_lists[depth]
  for i in range(len(curr_list)):
    print_list[depth] = curr_list[i]
    if depth == len(word_lists) - 1:
      print print_list
    else:
      looper(word_lists, print_list, depth + 1)

#### Test Cases ####

#setCombo([["apple", "banana", "pear"], ["car", "truck"], ["zambia", "malawi", "kenya"]])

digits = [0,1,2,3,4,5,6,7,8,9]
digits_one = [1,2,3,4,5,6,7,8,9]
# Easiest way to test solution, should count from 100 to 199
# setCombo([[1], digits, digits])
# 100 to 9999
# setCombo([digits_one, digits, digits, digits])

# Single list input
setCombo([digits])
setCombo([[1]])

setCombo([digits, ["x"]])

