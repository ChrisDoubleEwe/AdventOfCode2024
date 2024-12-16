import copy;
import sys
sys.setrecursionlimit(10000)
import re;
filename = '16_in.txt';




if filename == '16_in.txt':
  best = 160624;
if filename == '16_test2.txt':
  best = 11048;
if filename == '16_test1.txt':
  best = 7036;


parta = 0;
partb = 0;

map = [];

y = -1;
x = -1;
startx = -1;
starty = -1;
endx = -1;
endx = -1;

lowest_map = [];
views = [];

with open(filename) as f:
  for line in f:
    view_row = [];
    dir = [];
    dir.append(-1);
    dir.append(-1);
    dir.append(-1);
    dir.append(-1);

    y+=1;
    l = line.strip()
    if 'E' in l:
      endy = y;
    if 'S' in l:
      starty = y;
    row = [];
    score_row = [];
    x = -1;
    for c in l:
      view_row.append(0);
      score_row.append(copy.deepcopy(dir));
      x += 1;
      if c == 'S':
        row.append('.');
      else:
        row.append(c);

      if c == 'E':
        endx = x;
      if c == 'S':
        startx = x;
    map.append(copy.deepcopy(row));
    views.append(copy.deepcopy(view_row));
    lowest_map.append(copy.deepcopy(score_row));


best_paths = [];

#for r in map:
#  for c in r:
#    sys.stdout.write(c)
#  print('');

lowestscore = -1;

def go(y, x , d, score, steps, path):
  global lowestscore;
  global lowest_map;

  if score > best:
    return;
  if steps > 900:
    return;
  dnum = -1;
  if d == 'n':
    dnum = 0;
  if d == 'e':
    dnum = 1;
  if d == 's':
    dnum = 2;
  if d == 'w':
    dnum = 3;
  
  pair = ':--';
  pair+=str(y);
  pair+=',';
  pair+=str(x);
  pair+='--';
  if pair not in path:
    path+=pair;



  if lowest_map[y][x][dnum] > -1 and score > lowest_map[y][x][dnum]:
    return;

  lowest_map[y][x][dnum] = score;

  # Are we there yet?
  if x == endx and y == endy:
    print("Finished with score: " + str(score) + " ; steps=" + str(steps));
    best_paths.append(path);
    if lowestscore == -1 or score < lowestscore:
      lowestscore = score;

  if lowestscore > -1 and score > lowestscore:
    return;

  # Try step forward
  if d == 'e':
    if map[y][x+1] != '#':
      go(y, x+1, d, score+1, steps+1, path);
  elif d == 'w':
    if map[y][x-1] != '#':
      go(y, x-1, d, score+1, steps+1, path);
  elif d == 'n':
    if map[y-1][x] != '#':
      go(y-1, x, d, score+1, steps+1, path);
  elif d == 's':
    if map[y+1][x] != '#':
      go(y+1, x, d, score+1, steps+1, path);

  # Try turn CW
  if d == 'e':
    go(y, x, 's', score+1000, steps+1, path);
  elif d == 's':
    go(y, x, 'w', score+1000, steps+1, path);
  elif d == 'w':
    go(y, x, 'n', score+1000, steps+1, path);
  elif d == 'n':
    go(y, x, 'e', score+1000, steps+1, path);

  # Try turn CCW
  if d == 'w':
    go(y, x, 's', score+1000, steps+1, path);
  elif d == 'n':
    go(y, x, 'w', score+1000, steps+1, path);
  elif d == 'e':
    go(y, x, 'n', score+1000, steps+1, path);
  elif d == 's':
    go(y, x, 'e', score+1000, steps+1, path);






go(starty, startx, 'e', 0, 0, '');

for t in best_paths:
  print(t);

empty_views = copy.deepcopy(views);

print(len(best_paths));
for z in best_paths:
  views = copy.deepcopy(empty_views);
  print("xxxxxxxxxxxxxxxxxxxxxxx");
  z1 = z.split(':');
  print(z1);
  for z2 in z1:
    if z2 == '':
      continue;
    print(z2);
    z3 = z2.replace('-', '');
    print(z3);
    p = z3.split(',');
    print(p);
    views[int(p[0])][int(p[1])] = 1;

  print("+++++++++++++++++++++++++++++++++++++++++");

  for y in range(0, len(map)):
    for x in range(0, len(map[0])):
      if views[y][x] == 0:
        sys.stdout.write(map[y][x])
      else:
        sys.stdout.write('O')
    print('');


views = copy.deepcopy(empty_views);

for z in best_paths:
  z1 = z.split(':');
  for z2 in z1:
    if z2 == '':
      continue;
    z3 = z2.replace('-', '');
    p = z3.split(',');
    views[int(p[0])][int(p[1])] = 1;

for y in range(0, len(map)):
  for x in range(0, len(map[0])):
    if views[y][x] == 0:
      sys.stdout.write(map[y][x])
    else:
      sys.stdout.write('O')
  print('');


    
partb = 0;
for row in views:
  for c in row:
    if c == 1:
      partb += 1;

print("PART B: " + str(partb));
