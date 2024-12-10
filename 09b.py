import copy;
import sys
import re;
filename = '09_in.txt';

disk = []
file_size = {}
parta = 0;
partb = 0;

with open(filename) as f:
  for l in f:
    line = l.strip()

    id = -1;
    file = 1;
    for c in line:
      print(c);
      if file == 1:
        id += 1
        file_size[id] = int(c);
      for i in range(0, int(c)):
        if file == 1:
          disk.append(id);
        else:
          disk.append('.');
      if file == 1:
        file = 0;
      else:
        file = 1;




print("Starting disk layout:");
print(disk);

print("Compacting...");

done = 0;

for i in range(id, -1, -1):
  print("Doing " + str(i));
  #print("  file size = " + str(file_size[i]));

  space = 0;
  space_start = -1;
  space_length = -1;
  for j in range(0, len(disk)-1):
    if space_length == file_size[i] and space_start < disk.index(i):
      #print("Moving " + str(i));
      #print("  space_start=" + str(space_start));
      while i in disk:
        disk[disk.index(i)] = '.';
      for x in range(0, file_size[i]):
        disk[space_start+x]=i;
      break;
    if disk[j] == '.' and space == 0:
      space_start = j;
      space = 1;
      space_length = 1;
      continue;
    if disk[j] == '.' and space == 1:
      space_length += 1;
      continue;
    if disk[j] != '.':
      space_start = -1;
      space_length = -1;
      space = 0;
  #print(disk)



 
print("DONE");

print(disk)
checksum = 0;
for i in range(0,len(disk)-1):
  if disk[i] != '.':
    print('===');
    print("i: " + str(i));
    print("disk[i]: " + str(disk[i]));
    print("i*disk[i]: " + str((i*disk[i])));
    checksum += (i*disk[i]);
    print("csum: " + str(checksum)); 

print('------');
print(checksum);
