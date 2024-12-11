import copy;
import sys
import re;
filename = '11_in.txt';

map = []
empty_map = [];
temp_map = [];
parta = 0;
partb = 0;

stones = [];

with open(filename) as f:
  for l in f:
    line = l.strip()

    for x in line.split(' '):
      stones.append(int(x));

count = {};
count[0] = 0;
count[1] = 0;

for s in stones:
  count[s] = 1;

blink = 75;
for blinks in range(1, blink+1):
  new_count = copy.deepcopy(count)
  for key in list(count.keys()):
    if count[key] == 0:
      continue;
    if key == 0:
      n = count[key];
      new_count[0] -= n;
      new_count[1] += n;
      continue;
    if len(str(key)) % 2 == 0:
      half_one =  int(str(key)[0:len(str(key))//2]);
      half_two =  int(str(key)[len(str(key))//2:]); 
      n = count[key]
      new_count[key] -= n;
      if half_one in new_count:
        new_count[half_one] += n;
      else:
        new_count[half_one] = n;

      if half_two in new_count:
        new_count[half_two] += n;
      else:
        new_count[half_two] = n;
      continue;
    n = count[key]
    new_count[key] -= n;
    newkey = key*2024;
    if newkey in new_count:
      new_count[newkey] += n;
    else:
      new_count[newkey] = n;

  count = copy.deepcopy(new_count);
  c = 0;
  for key in list(count.keys()):
    c += count[key];
  if blinks == 25:
    parta = c
  if blinks == 75:
    partb = c

  


c = 0;
for key in list(count.keys()):
  c += count[key];
print("PART A: " + str(parta));
print("PART B: " + str(partb));

