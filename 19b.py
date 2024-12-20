import copy;
import sys
import math;
sys.setrecursionlimit(10000)
import re;
import functools;

filename = '19_in.txt';

parta = 0;
partb = 0;

towels = [];
patterns = [];

br = 0;
with open(filename) as f:
  for line in f:
    l = line.strip()
    if l == '':
      br = 1;
      continue;
    if br == 0:
      for t in l.split(', '):
        towels.append(t);
    else:
      patterns.append(l);

mem = {};

sorted_keys = sorted(towels, key=len)
sorted_keys.reverse();
towels = copy.deepcopy(sorted_keys);


@functools.cache
def how_many_different_ways(s):
  global mem;
  if s == '':
    return 1;
  if s in mem.keys():
    return mem[s]

  match = 0;
  total = 0;
  for t in towels:
    if s.startswith(t):
      match = 1;
      total += how_many_different_ways(s[len(t):]);
  mem[s] = total;
  return total;

total = 0;
count = 0;
valid_count = 0;
for p in patterns:
  count += 1
  print("----------")
  print("Doing " + str(count) + " : " + p);
  this_total = how_many_different_ways(p)
  print("TOTAL: " + str(this_total))
  if this_total > 0:
    valid_count += 1;
  total += this_total

print("PART A: " + str(valid_count));
print("PART B: " + str(total));

