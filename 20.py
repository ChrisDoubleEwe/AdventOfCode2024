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

cheats = [];
for x in range(1, len(map[0])):
  for y in range(1, len(map)):
    if dist_map[y][x] > -1:
      if x > 2:
        if dist_map[y][x-2] > dist_map[y][x] and dist_map[y][x-1] == -1 and dist_map[y][x-2] > -1:
          cheat = [];
          cheat.append(y);
          cheat.append(x);
          cheat.append(y);
          cheat.append(x-2);
          cheat.append(dist_map[y][x-2] - dist_map[y][x] - 2);
          cheats.append(copy.deepcopy(cheat));
      if x < len(map[0])-2:
        if dist_map[y][x+2] > dist_map[y][x] and dist_map[y][x+1] == -1 and dist_map[y][x+2] > -1:
          cheat = [];
          cheat.append(y);
          cheat.append(x);
          cheat.append(y);
          cheat.append(x+2);
          cheat.append(dist_map[y][x+2] - dist_map[y][x] - 2);
          cheats.append(copy.deepcopy(cheat));
      if y > 2:
        if dist_map[y-2][x] > dist_map[y][x] and dist_map[y-1][x] == -1 and dist_map[y-2][x] > -1:
          cheat = [];
          cheat.append(y);
          cheat.append(x);
          cheat.append(y-2);
          cheat.append(x);
          cheat.append(dist_map[y-2][x] - dist_map[y][x] - 2);
          cheats.append(copy.deepcopy(cheat));
      if y < len(map)-2:
        if dist_map[y+2][x] > dist_map[y][x] and dist_map[y+1][x] == -1 and dist_map[y+2][x] > -1:
          cheat = [];
          cheat.append(y);
          cheat.append(x);
          cheat.append(y+2);
          cheat.append(x);
          cheat.append(dist_map[y+2][x] - dist_map[y][x] - 2);
          cheats.append(copy.deepcopy(cheat));




parta = 0;
for i in range(0, racelength):
  num = 0
  for c in cheats:
    if c[4] == i:
      num += 1;
  if num > 0:
    print(str(num) + " cheats saving " + str(i));
  if i >= 100:
    parta += num;

print("PART A: " + str(parta));


  

      

