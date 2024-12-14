import copy;
import sys
import re;
filename = '12_in.txt';


map = []
parta = 0;
partb = 0;
crops = [];

with open(filename) as f:
  for l in f:
    line = l.strip()

    map.append(list(line));
    for c in line:
      if c not in crops:
        crops.append(c);
print(crops);
max_x = len(map);
max_y = len(map[0]);

new_map = [];
empty_row = [];
for i in range(0, len(map[0])+2):
  empty_row.append('.');
new_map.append(copy.deepcopy(empty_row));
for r in map:
  new_row = [];
  new_row.append('.');
  for c in r:
    new_row.append(c);
  new_row.append('.');
  new_map.append(copy.deepcopy(new_row));
new_map.append(copy.deepcopy(empty_row));

map = copy.deepcopy(new_map);

for r in map:
  print(r)

regions = [];
for x in range(1, max_x+1):
  for y in range(1, max_y+1):
    if map[y][x] == '.':
      continue;
    print(map[y][x]);
    region = [];
    region.append(map[y][x]);
    region.append(y);
    region.append(x);
    regions.append(copy.deepcopy(region));

combo_reg = [];

for r in regions:
  this_combo = [];
  this_combo.append(r);
  for x in regions:
    if r == x:
      continue;
    if r[0] != x[0]:
      continue;
    if r[1] == x[1] and abs(r[2]-x[2]) == 1:
      this_combo.append(x);
      continue;
    if r[2] == x[2] and abs(r[1]-x[1]) == 1:
      this_combo.append(x);
      continue;
  combo_reg.append(copy.deepcopy(this_combo));

for c in combo_reg:
  print(c);

merge = [];
done_merge = 1;
a_min = 0;
while done_merge == 1:
  done_merge = 0;
  for a in range(a_min, len(combo_reg)):
    if done_merge == 1:
      break;
    for b in range(a_min, len(combo_reg)):
      if done_merge == 1:
        break;

      if a == b:
        continue;
      for i in combo_reg[a]:
        if done_merge == 1:
          break;
        for j in combo_reg[b]:
          if i == j:
            print("merging" + str(a) + " and " + str(b) + " (" + str(len(combo_reg))+ ")");
            done_merge = 1;
            for z in combo_reg[b]:
              if z not in combo_reg[a]:
                combo_reg[a].append(z);
            del combo_reg[b];
            break;
    a_min = a;

lengths = [];

for r in combo_reg:
  l = 0;
  for b in r:
    c = b[0];
    y = b[1];
    x = b[2];
  
    corners = 0;
    if map[y][x+1] != c and map[y+1][x] != c:
      print(c + " - ext lower-right corner at x=" + str(x) + " ; y=" + str(y));
      corners+=1;
    if map[y][x+1] != c and map[y-1][x] != c:
      print(c + " - ext upper-right corner at x=" + str(x) + " ; y=" + str(y));
      corners+=1;
    if map[y][x-1] != c and map[y+1][x] != c:
      print(c + " - ext lower-leftt corner at x=" + str(x) + " ; y=" + str(y));
      corners+=1;
    if map[y][x-1] != c and map[y-1][x] != c:
      print(c + " - ext upper-left corner at x=" + str(x) + " ; y=" + str(y));
      corners+=1;

    if map[y][x+1] == c and map[y+1][x] == c and map[y+1][x+1] != c:
      print(c + " - int lower-right corner at x=" + str(x) + " ; y=" + str(y));
      corners+=1;
    if map[y][x+1] == c and map[y-1][x] == c and map[y-1][x+1] != c:
      print(c + " - int upper-right corner at x=" + str(x) + " ; y=" + str(y));
      corners+=1;
    if map[y][x-1] == c and map[y+1][x] == c and map[y+1][x-1] != c:
      print(c + " - int lower-leftt corner at x=" + str(x) + " ; y=" + str(y));
      corners+=1;
    if map[y][x-1] == c and map[y-1][x] == c and map[y-1][x-1] != c:
      print(c + " - int upper-left corner at x=" + str(x) + " ; y=" + str(y));
      corners+=1;



    l += corners;
  lengths.append(l)

for i in range(0, len(combo_reg)):
  res = lengths[i] * len(combo_reg[i]);
  print(combo_reg[i][0][0] + ": " + str(len(combo_reg[i])) + ' * ' + str(lengths[i]) + ' = ' + str(res))
  parta += res;

print("PART B: " + str(parta));



  
