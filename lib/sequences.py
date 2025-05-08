#!/usr/bin/env python3

def print_fibonacci(length):
   if length == 0:
      print ([])
      return 

   sequence = [0]
   if length == 1:
      print (sequence)
      return 
      
   
   sequence.append(1)
   for i in range (2, length):
      next_value = sequence[-1] + sequence[-2]
      sequence.append(next_value)

   print (sequence)