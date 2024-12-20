import copy;
import sys
import math;
sys.setrecursionlimit(10000)
import re;
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

print(towels);
print(patterns);

p_count = 0
possible_count = 0;
for p in patterns:
  p_count += 1;
  print("Doing pattern: " + p + "   -  " + str(p_count) + ' / ' + str(len(patterns)));
  possibles = [''];
  done = 0;
  this_p = copy.deepcopy(p);
  this_is_possible = 0;
  while done == 0:
    #print(len(possibles));
    #print(possibles);
    new_possibles = [];
    if len(possibles) == 0:
      break;
    for pos in possibles:
      for t in towels:
        this_pos = pos + t
        if p == this_pos:
          done = 1;
          this_is_possible = 1;
        elif p.startswith(this_pos):
          #print('  ' + this_pos);
          new_possibles.append(this_pos);
    possibles = copy.deepcopy(list(set(new_possibles)));
  if this_is_possible == 0:
    print("  Impossible");
  else:
    print("  Possible");
    possible_count += 1;

print("PART A: " + str(possible_count));

          
    
