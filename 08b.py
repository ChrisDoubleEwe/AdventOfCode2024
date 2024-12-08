import copy;
import sys
import re;
filename = '08_in.txt';

map = []
amap = [];
parta = 0;
partb = 0;

with open(filename) as f:
  for l in f:
    line = l.strip()

    map.append(list(line));

blank_row = [];
for x in range(0, len(map[0])):
  blank_row.append('.');
for y in range(0, len(map)):
  amap.append(copy.deepcopy(blank_row));



freq = [];
ants = {};
nodes = [];
for x in range(0, len(map[0])):
  for y in range(0, len(map)):
    f = map[y][x];
    if f != '.':
      if f not in freq:
        freq.append(f); 
      if f not in ants:
        ants[f] = [];
      pair = [];
      pair.append(y);
      pair.append(x);
      ants[f].append(pair);


      

for f in freq:
  for i in range(0, len(ants[f])):
    for j in range(i, len(ants[f])):
      if i == j:
        continue;
      y_diff = ants[f][i][0] - ants[f][j][0];
      x_diff = ants[f][i][1] - ants[f][j][1];

      # Go backwards
      stepx = int(len(map[0])/abs(x_diff))+3;
      stepy = int(len(map)/abs(y_diff))+3;
      step = stepy;
      if stepx > stepy:
        step = stepx;

      for m in range(0, step):
        a1y = ants[f][i][0]+(y_diff*m);
        a1x = ants[f][i][1]+(x_diff*m);
        a1_pair = [];
        a1_pair.append(a1y);
        a1_pair.append(a1x);
        if a1y >= 0 and a1y < len(map):
          if a1x >= 0 and a1x < len(map[0]):
            if a1_pair not in nodes:
              nodes.append(a1_pair);
              amap[a1y][a1x] = f;
        # Go forwards
        a2y = ants[f][j][0]-(y_diff*m);
        a2x = ants[f][j][1]-(x_diff*m);
        a2_pair = [];
        a2_pair.append(a2y);
        a2_pair.append(a2x);
        if a2y >= 0 and a2y < len(map):
          if a2x >= 0 and a2x < len(map[0]):
            if a2_pair not in nodes:
              nodes.append(a2_pair);
              amap[a2y][a2x] = f;



partb = len(nodes);

      
print("PART B: " + str(partb));

