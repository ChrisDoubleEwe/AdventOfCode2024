import copy;
import matplotlib.pyplot as plt

import sys
import re;
filename = '14_in.txt';
if filename == '14_in.txt':
  map_x = 101;
  map_y = 103;
  t = 100;
else:
  map_x = 11;
  map_y = 7;
  t = 100;




parta = 0;
partb = 0;

guards = [];


with open(filename) as f:
  for line in f:
    l = line.strip()

    g = [];
    p = l.split(' ')[0];
    px = int(p.split(',')[0][2:]);
    py = int(p.split(',')[1]);
    v = l.split(' ')[1];
    vx = int(v.split(',')[0][2:]);
    vy = int(v.split(',')[1]);

    gp = [];
    gp.append(px);
    gp.append(py);
    gv = [];
    gv.append(vx);
    gv.append(vy);
    g.append(copy.deepcopy(gp));
    g.append(copy.deepcopy(gv));
    line = l.strip()
    guards.append(copy.deepcopy(g));


quads = [0, 0, 0, 0];
mid_x = (map_x-1)/2;
mid_y = (map_y-1)/2;

empty_map = [];
empty_row = [];
for x in range(0, map_x):
  empty_row.append(0);
for y in range(0, map_y):
  empty_map.append(copy.deepcopy(empty_row));


t = -1;
cont = 1;
while cont == 1:
  t += 1;
  if (t % 10)==0:
    print(t)
  if t > 10000:
    cont = 0;
  map = copy.deepcopy(empty_map);
  br = 0;
  for g in guards:
    posx = (g[0][0] + (g[1][0] * t)) % map_x;
    posy = (g[0][1] + (g[1][1] * t)) % map_y;
    if map[posy][posx] == 255:
      br = 1;
      break;
    map[posy][posx] = 255;
  if br == 1:
    continue;

  print("PART B: " + str(t));
  cont = 0;

  image_file = '14_image.png';
  plt.imshow(map, interpolation='nearest', cmap='gray')
  plt.savefig(image_file)




