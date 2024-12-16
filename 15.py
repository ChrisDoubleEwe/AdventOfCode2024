import copy;
import sys
import re;
filename = '15_in.txt';

parta = 0;
partb = 0;

map = [];
instr = [];


br = 0;
with open(filename) as f:
  for line in f:
    l = line.strip()

    if l == '':
      br = 1;
      continue;

    if br == 0:
      row = [];
      for c in l:
        row.append(c);
      map.append(copy.deepcopy(row));
    else:
      for c in l:
        instr.append(c);


print("Initial state:");

x = -1;
y = -1;

this_y = -1;
for m in map:
  this_y += 1;
  this_x = -1;
  for c in m:
    this_x += 1;
    sys.stdout.write(c)
    if c == '@':
      x = this_x;
      y = this_y;
  print('');

for i in instr:
  print(' ');
  print("Move: " + str(i))

  if i == '<':
    if map[y][x-1] == '.':
      map[y][x] = '.';
      x = x-1;
      map[y][x] = '@';
    else:
      if map[y][x-1] == 'O':
        inc = 0;
        hit_wall = 0;
        hit_space = 0;
        while hit_wall == 0 and hit_space == 0:
          inc+=1;
          if map[y][x-1-inc] == '.':
            hit_space = 1;
            map[y][x-1-inc] = 'O';
            map[y][x-1] = '.';
            map[y][x] = '.';
            x = x-1;
            map[y][x] = '@';
          if map[y][x-1-inc] == '#':
            hit_wall = 1;

  if i == '>':
    if map[y][x+1] == '.':
      map[y][x] = '.';
      x = x+1;
      map[y][x] = '@';
    else:
      if map[y][x+1] == 'O':
        inc = 0;
        hit_wall = 0;
        hit_space = 0;
        while hit_wall == 0 and hit_space == 0:
          inc+=1;
          if map[y][x+1+inc] == '.':
            hit_space = 1;
            map[y][x+1+inc] = 'O';
            map[y][x+1] = '.';
            map[y][x] = '.';
            x = x+1;
            map[y][x] = '@';
          if map[y][x+1+inc] == '#':
            hit_wall = 1;


  if i == '^':
    if map[y-1][x] == '.':
      map[y][x] = '.';
      y = y-1;
      map[y][x] = '@';
    else:
      if map[y-1][x] == 'O':
        inc = 0;
        hit_wall = 0;
        hit_space = 0;
        while hit_wall == 0 and hit_space == 0:
          inc+=1;
          if map[y-1-inc][x] == '.':
            hit_space = 1;
            map[y-1-inc][x] = 'O';
            map[y-1][x] = '.';
            map[y][x] = '.';
            y = y-1;
            map[y][x] = '@';
          if map[y-1-inc][x] == '#':
            hit_wall = 1;

  if i == 'v':
    if map[y+1][x] == '.':
      map[y][x] = '.';
      y = y+1;
      map[y][x] = '@';
    else:
      if map[y+1][x] == 'O':
        inc = 0;
        hit_wall = 0;
        hit_space = 0;
        while hit_wall == 0 and hit_space == 0:
          inc+=1;
          if map[y+1+inc][x] == '.':
            hit_space = 1;
            map[y+1+inc][x] = 'O';
            map[y+1][x] = '.';
            map[y][x] = '.';
            y = y+1;
            map[y][x] = '@';
          if map[y+1+inc][x] == '#':
            hit_wall = 1;

    

  for m in map:
    for c in m:
      sys.stdout.write(c)
    print('');


this_y = -1;
for m in map:
  this_y += 1;
  this_x = -1;
  for c in m:
    this_x += 1;
    if c == 'O':
      parta += (100 * this_y);
      parta += this_x;

print("PART A: " + str(parta));
