import copy;
import itertools
import os;
import sys
import math;
sys.setrecursionlimit(10000)
import re;
filename = '25_in.txt';

parta = 0;
partb = 0;

keys = [];
locks = [];
key = []
lock = []

br = 1;
with open(filename) as f:
  for line in f:
    print(line);
    if line.strip() == '':
      br = 1;
      print("BREAK");
      if schematic[0][0]=='.':
        keys.append(copy.deepcopy(schematic));
      else:
        locks.append(copy.deepcopy(schematic));
      continue;
    else:
      if br == 1:
        schematic = [];
        schematic.append(list(line.strip()));
        br = 0;
      else:
        schematic.append(list(line.strip()));

# GET LAST ONE
if schematic[0][0]=='.':
  keys.append(copy.deepcopy(schematic));
else:
  locks.append(copy.deepcopy(schematic));



print(locks);
print("================");
print(keys);

# "So, you could say the first lock has pin heights 0,5,3,4,3:"

# #####
# .####
# .####
# .####
# .#.#.
# .#...
# .....

for l in locks:
  for row in l:
    print(row);

  tumbler = [0,0,0,0,0]
  for height in range(1, 6):
    for t in range(0, 5):
      if l[height][t] == '#':
        tumbler[t] += 1;

  print(tumbler);

  lock.append(copy.deepcopy(tumbler));

# "Or, that the first key has heights 5,0,2,1,3:"

# .....
# #....
# #....
# #...#
# #.#.#
# #.###
# #####

for k in keys:
  for row in k:
    print(row);

  tumbler = [0,0,0,0,0]
  for height in range(0, 6):
    for t in range(0, 5):
      if k[height][t] == '#':
        tumbler[t] += 1;

  print(tumbler);

  key.append(copy.deepcopy(tumbler));


for l in lock:
  for k in key:

    fit = 1;
    for t in range(0, 5):
      if l[t] + k[t] >  5:
        fit = 0;
    if fit == 0:
      print("  Lock " + str(l) + " and key " + str(k) + " OVERLAPS");
    else:
      print("  Lock " + str(l) + " and key " + str(k) + " FITS");
      parta += 1;

print("PART A: " + str(parta));
