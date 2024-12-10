import copy;
import sys
import re;
filename = '10_in.txt';

map = []
empty_map = [];
temp_map = [];
parta = 0;
partb = 0;

with open(filename) as f:
  for l in f:
    line = l.strip()

    row = [-1]
    empty_row = [-1,-1];
    for c in list(line):
      if c == '.':
        row.append(-1);
      else:
        row.append(int(c));
      empty_row.append(-1);
    row.append(-1);
    map.append(copy.deepcopy(row));
    empty_map.append(copy.deepcopy(empty_row));
  temp_map = [];
  temp_map.append(empty_row);
  for r in map:
    temp_map.append(copy.deepcopy(r));
  temp_map.append(empty_row);
  map = copy.deepcopy(temp_map);

  temp_map = [];
  temp_map.append(empty_row);
  for r in empty_map:
    temp_map.append(copy.deepcopy(r));
  temp_map.append(empty_row);
  empty_map = copy.deepcopy(temp_map);





zeroes = [];

for y in range(0, len(map)):
  for x in range(0, len(map[0])):
    if map[y][x] == 0:
      pair = [];
      pair.append(x);
      pair.append(y);
      zeroes.append(pair);


# Find trails
scores = [];
this_map = copy.deepcopy(empty_map);

for z in zeroes:
  this_map = copy.deepcopy(empty_map);

  this_map[z[1]][z[0]] = 0;

  count = -1;
  while count < 10:
    count += 1

    for y in range(0, len(map)):
      for x in range(0, len(map[0])):
        if this_map[y][x] == count:
          if map[y][x+1] == count+1:
            this_map[y][x+1] = count+1;
          if map[y][x-1] == count+1:
            this_map[y][x-1] = count+1;
          if map[y+1][x] == count+1:
            this_map[y+1][x] = count+1;
          if map[y-1][x] == count+1:
            this_map[y-1][x] = count+1;

  score = 0;
  for y in range(0, len(map)):
    for x in range(0, len(map[0])):
      if this_map[y][x] == 9:
        score += 1;

  scores.append(score);

  
for s in scores:
  parta += s;

print("PART A: " + str(parta));

# Calculate ratings

paths = []
for z in zeroes:
  path = [];
  path.append(copy.deepcopy(z));
  paths.append(copy.deepcopy(path));

for i in range(1, 10):
  new_paths = []
  for pa in paths:
    p = pa[-1];
    x = p[0];
    y = p[1];

    if map[y][x+1] == i:
      new_path = [];
      new_path.append(copy.deepcopy(p));
      pair = [];
      pair.append(x+1)
      pair.append(y)
      new_path.append(copy.deepcopy(pair));
      new_paths.append(copy.deepcopy(new_path));
    if map[y][x-1] == i:
      new_path = [];
      new_path.append(copy.deepcopy(p));
      pair = [];
      pair.append(x-1)
      pair.append(y)
      new_path.append(copy.deepcopy(pair));
      new_paths.append(copy.deepcopy(new_path));
    if map[y-1][x] == i:
      new_path = [];
      new_path.append(copy.deepcopy(p));
      pair = [];
      pair.append(x)
      pair.append(y-1)
      new_path.append(copy.deepcopy(pair));
      new_paths.append(copy.deepcopy(new_path));
    if map[y+1][x] == i:
      new_path = [];
      new_path.append(copy.deepcopy(p));
      pair = [];
      pair.append(x)
      pair.append(y+1)
      new_path.append(copy.deepcopy(pair));
      new_paths.append(copy.deepcopy(new_path));
  paths = copy.deepcopy(new_paths);

print("PART B: " + str(len(paths)));







  
