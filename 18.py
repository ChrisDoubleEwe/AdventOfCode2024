import copy;
import sys
import math;
sys.setrecursionlimit(10000)
import re;
filename = '';
max_x = -1;
may_y = -1;
test = 0;

if test == 1:
  filename = '18_test1.txt';
  max_x = 6;
  max_y = 6;
  bytes = 12;
if test == 0:
  filename = '18_in.txt';
  max_x = 70;
  max_y = 70;
  bytes = 1024;

parta = 0;
partb = 0;

borderchar = '+';
map = [];
dist_map = [];
row = [];
border = [];
row.append(borderchar);
for x in range(0, max_x+1):
  row.append('.');
  border.append(borderchar);
row.append(borderchar);

border.append(borderchar);
border.append(borderchar);
map.append(copy.deepcopy(border));
for y in range(0, max_y+1):
  map.append(copy.deepcopy(row));
map.append(copy.deepcopy(border));


memory = [];
with open(filename) as f:
  for line in f:
    l = line.strip()
    if len(l) < 1:
      continue;
    x = int(l.split(',')[0])+1;
    y = int(l.split(',')[1])+1;
    pair = [];
    pair.append(y);
    pair.append(x);
    memory.append(copy.deepcopy(pair));


count = -1;
while count+1 < bytes:
  count += 1;
  x = memory[count][1];
  y = memory[count][0];
  map[y][x] = '#';

startval = 999999999999;
for m in map:
  dist_row = [];
  for c in m:
    if c == '.':
      dist_row.append(startval);
    else:
      dist_row.append(-1);
    sys.stdout.write(c)
  dist_map.append(copy.deepcopy(dist_row));
  print('');

print(dist_map);
print('==================');
dist_map[1][1] = 0;
carryon = 1;
while carryon == 1:
  carryon = 0
  for x in range(1, max_x+2):
    for y in range(1, max_y+2):
      print('Doing x: ' + str(x) + ' ; y: ' + str(y) + ' (val=' + str(dist_map[y][x]) + ' )');
      if dist_map[y][x] > -1 and dist_map[y][x] < startval:
        print('Cell val = ' + str(dist_map[y][x]));
        if dist_map[y][x+1] == startval:
          dist_map[y][x+1] = dist_map[y][x] + 1;
          carryon = 1;
          print("carryon=" + str(carryon));

        if dist_map[y][x-1] == startval:
          dist_map[y][x-1] = dist_map[y][x] + 1;
          carryon = 1;
          print("carryon=" + str(carryon));

        if dist_map[y+1][x] == startval:
          dist_map[y+1][x] = dist_map[y][x] + 1;
          carryon = 1;
          print("carryon=" + str(carryon));

        if dist_map[y-1][x] == startval:
          dist_map[y-1][x] = dist_map[y][x] + 1;
          carryon = 1;
          print("carryon=" + str(carryon));

  print("Final carryon=" + str(carryon));

for m in dist_map:
  print(m);

print("PART A:")
print(dist_map[max_y+1][max_x+1]);
