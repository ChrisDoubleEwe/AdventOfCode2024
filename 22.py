import copy;
import itertools

import os;
import sys
import math;
sys.setrecursionlimit(10000)
import re;
filename = '22_in.txt';

parta = 0;
partb = 0;

inits = [];
with open(filename) as f:
  for line in f:
    l = line.strip()
    inits.append(int(l));

print(inits);



def mix(x, y):
  return x ^ y;

def prune(x):
  return x % 16777216;

def next(secret):
  # Calculate the result of multiplying the secret number by 64.
  a = secret * 64;

  # Then, mix this result into the secret number.
  secret = mix(secret, a);

  # Finally, prune the secret number.
  secret = prune(secret);

  # Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. 
  d = secret // 32

  # Then, mix this result into the secret number.
  secret = mix(secret, d);

  # Finally, prune the secret number.
  secret = prune(secret);

  # Calculate the result of multiplying the secret number by 2048.
  g = secret * 2048;

  # Then, mix this result into the secret number.
  secret = mix(secret, g);

  # Finally, prune the secret number.
  secret = prune(secret);

  return(secret);


parta = 0;

for i in inits:
  print('------');
  print(i);
  this_num = i;
  for z in range(0, 2000):
    num = next(this_num);
    this_num = num;
  parta += this_num;
  print(this_num);

print("PART A: " + str(parta));

