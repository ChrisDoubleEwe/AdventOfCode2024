import copy;
import sys
import re;
filename = '09_in.txt';

disk = []
parta = 0;
partb = 0;

with open(filename) as f:
  for l in f:
    line = l.strip()

    id = -1;
    file = 1;
    for c in line:
      if file == 1:
        id += 1
      for i in range(0, int(c)):
        if file == 1:
          disk.append(id);
        else:
          disk.append('.');
      if file == 1:
        file = 0;
      else:
        file = 1;




print("Compacting...");

done = 0;

while done == 0:
  first_dot = disk.index('.');
  last_num = -1;
  for i in range(len(disk)-1,-1,-1):
    if disk[i] != '.':
      last_num = i;
      break;
  if first_dot > last_num:
    done = 1;
    break;
  disk[first_dot] = disk[last_num];
  disk[last_num] = '.';

print("DONE");

checksum = 0;
for i in range(0,len(disk)-1):
  if disk[i] != '.':
    checksum += (i*disk[i]);

print("PART A: " + str(checksum));
