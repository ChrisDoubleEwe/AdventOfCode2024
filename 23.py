import copy;
import itertools
import os;
import sys
import math;
sys.setrecursionlimit(10000)
import re;
filename = '23_in.txt';

parta = 0;
partb = 0;

pairs = [];
computers = [];
with open(filename) as f:
  for line in f:
    l = line.strip().split('-');
    p = [];
    p.append(l[0]);
    p.append(l[1]);
    computers.append(p[0]);
    computers.append(p[1]);


    pairs.append(copy.deepcopy(p));

computers = copy.deepcopy(list(set(computers)));

groups_of_three = [];

t1_count = -1;
for z in pairs:
  t1 = z[0]
  t2 = z[1];
  t1_count += 1;
  print(str(t1_count) + ' / ' + str(len(pairs)));
  for t3 in computers:
    if t1 == t2 or t1 == t3 or t2 == t3:
      continue;
    t1_t3 = []
    t2_t3 = [];
    t1_t3.append(t1)
    t1_t3.append(t3)
    t2_t3.append(t2)
    t2_t3.append(t3)
    t3_t2 = copy.deepcopy(t2_t3);
    t3_t2.reverse();
    t3_t1 = copy.deepcopy(t1_t3);
    t3_t1.reverse();


    if t1_t3 in pairs or t3_t1 in pairs:
      if t2_t3 in pairs or t3_t2 in pairs:
        triplet = [];
        triplet.append(t1);
        triplet.append(t2);
        triplet.append(t3);
        sorted_triplet = sorted(triplet)
        if sorted_triplet not in groups_of_three:
          groups_of_three.append(copy.deepcopy(sorted_triplet));






for g in groups_of_three:
  for c in g:
    if c.startswith('t'):
      parta += 1;
      print(g);
      break;

print("PART A: " + str(parta));
