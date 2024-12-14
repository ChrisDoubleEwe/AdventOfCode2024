import copy;
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


for g in guards:
  posx = (g[0][0] + (g[1][0] * t)) % map_x;
  posy = (g[0][1] + (g[1][1] * t)) % map_y;
  if (posx > mid_x) and (posy > mid_y):
    quads[3] += 1;
  if (posx > mid_x) and (posy < mid_y):
    quads[2] += 1;
  if (posx < mid_x) and (posy > mid_y):
    quads[1] += 1;
  if (posx < mid_x) and (posy < mid_y):
    quads[0] += 1;



parta = quads[0] * quads[1] * quads[2] * quads[3]
print("PART A: " + str(parta));



