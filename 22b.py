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

result = [];
for i in inits:
  prices = [];
  this_num = i;
  for z in range(1, 2000):
    num = next(this_num);
    change = (num % 10) - (this_num % 10);
    price = num % 10;
    pair = []
    pair.append(price);
    pair.append(change);
    this_num = num;
    prices.append(copy.deepcopy(pair));
  result.append(copy.deepcopy(prices));



res_string = [];

for r in result:
  r_str = ''
  for p in r:
    if p[1] >= 0:
      r_str+= '+';
    r_str+= str(p[1]);

  res_string.append(copy.deepcopy(r_str));

max_val = -1;
for p1 in range(-9, 10):
  for p2 in range(-9, 10):
    for p3 in range(-9, 10):
      print(p1, p2, p3);
      for p4 in range(-9, 10):

        partb = 0;
        look_for = '';
        if p1 >= 0:
          look_for+='+';
        look_for += str(p1);
        if p2 >= 0:
          look_for+='+';
        look_for += str(p2);
        if p3 >= 0:
          look_for+='+';
        look_for += str(p3);
        if p4 >= 0:
          look_for+='+';
        look_for += str(p4);

        r_count = -1;
        for r in res_string:
          r_count += 1;
          pos = r.find(look_for)
          if pos > -1:
            val = result[r_count][(pos//2)+3][0]
            partb+= val;
        if partb > max_val:
          max_val = partb 

  
partb=max_val
print("PART B: " + str(partb));
