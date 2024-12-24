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

groups = {};
for c in computers:
  groups[c] = [];
  groups[c].append(c);

  
for p in pairs:
  if p[1] not in groups[p[0]]:
    groups[p[0]].append(p[1]);
  if p[0] not in groups[p[1]]:
    groups[p[1]].append(p[0]);

longest = [];
longest_count = -1;
gcount = 0
for g in groups:
  gcount += 1;
  #print("Doing "+ str(gcount) + " / " + str(len(groups)));
  results = [];
  for member in groups[g]:
    if member == g:
      continue;
    connections = 0;
    this_result = [];
    this_result.append(member);
    for to in groups[g]:
      if to == member:
        continue;
      lookfor = [];
      lookfor.append(to);
      lookfor.append(member);
      lookforrev = copy.deepcopy(lookfor);
      lookforrev.reverse();
      if lookfor in pairs or lookforrev in pairs:
        connections += 1;
        this_result.append(to);
    tr = sorted(this_result);
    results.append(copy.deepcopy(tr));
  best_result = -1;
  best = [];
  for r in results:
    count = results.count(r);

    if count > best_result:
      best_result = count
      best = copy.deepcopy(r);
  if best_result > longest_count:
    longest_count = best_result;
    longest = copy.deepcopy(best);


print("PART B");
print(','.join(longest));

