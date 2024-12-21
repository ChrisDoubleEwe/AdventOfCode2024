import copy;
import os;
import sys
import math;
sys.setrecursionlimit(10000)
import re;
filename = '20_in.txt';

parta = 0;
partb = 0;

map = [];
empty_dist = [];
sy = -1;
sx = -1;
ey = -1;
ex = -1;

y = -1
with open(filename) as f:
  for line in f:
    y += 1;
    x = -1;
    row = []
    dist_row = [];
    l = line.strip()
    for c in l:
      dist_row.append(-1);
      x += 1;
      if c == 'S':
        sx = x;
        sy = y;
        row.append('.');
      elif c == 'E':
        ex = x;
        ey = y;
        row.append('.');
      else:
        row.append(c);
    map.append(copy.deepcopy(row));
    empty_dist.append(copy.deepcopy(dist_row));

orig_map = copy.deepcopy(map);

for m in map:
  print(m);

for m in empty_dist:
  print(m);

dist_map = copy.deepcopy(empty_dist);

dist_map[sy][sx] = 0;

x = sx
y = sy
while dist_map[ey][ex] == -1:
  if dist_map[y][x] > -1:
    if map[y+1][x] == '.' and dist_map[y+1][x] == -1:
      dist_map[y+1][x] = dist_map[y][x] + 1;
      y += 1;
    if map[y-1][x] == '.' and dist_map[y-1][x] == -1:
      dist_map[y-1][x] = dist_map[y][x] + 1;
      y -= 1;
    if map[y][x+1] == '.' and dist_map[y][x+1] == -1:
      dist_map[y][x+1] = dist_map[y][x] + 1;
      x += 1;
    if map[y][x-1] == '.' and dist_map[y][x-1] == -1:
      dist_map[y][x-1] = dist_map[y][x] + 1;
      x -= 1;
  #os.system('clear')
  #for m in dist_map:
  #  print(m);

print(dist_map[ey][ex]);
racelength = dist_map[ey][ex];
print(racelength);

cheats = [];
for x in range(1, len(map[0])):
  print ("Done " + str(x) + " out of " + str(len(map[0])));
  for y in range(1, len(map)):
    for xmod in range(0,21):
      for ymod in range(0,21):
        if xmod + ymod > 20:
          break;
        if dist_map[y][x] > -1:
          if x - xmod > 0 and y - ymod > 0:
            if (dist_map[y-ymod][x-xmod] > dist_map[y][x] + xmod + ymod) and (dist_map[y-ymod][x-xmod] > -1):
              #print("Cheat from y=" + str(y) + ",x=" + str(x) + " to y=" + str(y-ymod) + ", x=" + str(x-xmod) + " : going from " + str(dist_map[y][x]) + " to " + str(dist_map[y-ymod][x-xmod]) + " saving " + str(dist_map[y-ymod][x-xmod] - dist_map[y][x] - xmod - ymod));
              cheat = [];
              cheat.append(y);
              cheat.append(x);
              cheat.append(y-ymod);
              cheat.append(x-xmod);
              cheat.append(dist_map[y-ymod][x-xmod] - dist_map[y][x] - xmod - ymod);
              if cheat[4] >= 100:
                cheats.append(copy.deepcopy(cheat));
          if x - xmod > 0 and y + ymod < len(map):
            if (dist_map[y+ymod][x-xmod] > dist_map[y][x] + xmod + ymod) and (dist_map[y+ymod][x-xmod] > -1):
              #print("Cheat from y=" + str(y) + ",x=" + str(x) + " to y=" + str(y+ymod) + ", x=" + str(x-xmod) + " : going from " + str(dist_map[y][x]) + " to " + str(dist_map[y+ymod][x-xmod]) + " saving " + str(dist_map[y+ymod][x-xmod] - dist_map[y][x] - xmod - ymod));
              cheat = [];
              cheat.append(y);
              cheat.append(x);
              cheat.append(y+ymod);
              cheat.append(x-xmod);
              cheat.append(dist_map[y+ymod][x-xmod] - dist_map[y][x] - xmod - ymod);
              if cheat[4] >= 100:
                cheats.append(copy.deepcopy(cheat));
          if x + xmod < len(map[0]) and y + ymod < len(map):
            if (dist_map[y+ymod][x+xmod] > dist_map[y][x] + xmod + ymod) and (dist_map[y+ymod][x+xmod] > -1):
              #print("Cheat from y=" + str(y) + ",x=" + str(x) + " to y=" + str(y+ymod) + ", x=" + str(x+xmod) + " : going from " + str(dist_map[y][x]) + " to " + str(dist_map[y+ymod][x+xmod]) + " saving " + str(dist_map[y+ymod][x+xmod] - dist_map[y][x] - xmod - ymod));

              cheat = [];
              cheat.append(y);
              cheat.append(x);
              cheat.append(y+ymod);
              cheat.append(x+xmod);
              cheat.append(dist_map[y+ymod][x+xmod] - dist_map[y][x] - xmod - ymod);
              if cheat[4] >= 100:
                cheats.append(copy.deepcopy(cheat));
          if x + xmod < len(map[0]) and y - ymod > 0:
            if (dist_map[y-ymod][x+xmod] > dist_map[y][x] + xmod + ymod) and (dist_map[y-ymod][x+xmod] > -1):
              #print("Cheat from y=" + str(y) + ",x=" + str(x) + " to y=" + str(y-ymod) + ", x=" + str(x+xmod) + " : going from " + str(dist_map[y][x]) + " to " + str(dist_map[y-ymod][x+xmod]) + " saving " + str(dist_map[y-ymod][x+xmod] - dist_map[y][x] - xmod - ymod));

              cheat = [];
              cheat.append(y);
              cheat.append(x);
              cheat.append(y-ymod);
              cheat.append(x+xmod);
              cheat.append(dist_map[y-ymod][x+xmod] - dist_map[y][x] - xmod - ymod);
              if cheat[4] >= 100:
                cheats.append(copy.deepcopy(cheat));



print("DONE");
new_cheats = [];


c_count = 0;
sorted_cheats = sorted(cheats); 
for s in sorted_cheats:
  print(s)

last = '';
for c in sorted_cheats:
  c_count += 1;
  if c_count % 100 == 0:
    print("Done " + str(c_count) + " out of " + str(len(cheats)));
  print("Is " + str(c) + " equal to " + str(last));
  if c == last:
    print("Remove duplicate");
    continue;
  new_cheats.append(copy.deepcopy(c));
  last = copy.deepcopy(c);
  #print(c);

cheats = copy.deepcopy(new_cheats);
for c in cheats:
  print(c)

for m in dist_map:
  print(m);

print("--------");
partb = 0;
for i in range(100, racelength):
  num = 0
  for c in cheats:
    if c[4] == i:
      num += 1;
      #print(c);
  if num > 0:
    print(str(num) + " cheats saving " + str(i));
    if i >= 100:
      partb += num;

print("PART B: " + str(partb));


  

      

