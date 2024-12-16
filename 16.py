import copy;
import sys
sys.setrecursionlimit(10000)
import re;
filename = '16_in.txt';

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
with open(filename) as f:
  for line in f:
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
    lowest_map.append(copy.deepcopy(score_row));




#for r in map:
#  for c in r:
#    sys.stdout.write(c)
#  print('');

lowestscore = -1;

def go(y, x , d, score, steps):
  global lowestscore;
  global lowest_map;

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


  if lowest_map[y][x][dnum] > -1 and score > lowest_map[y][x][dnum]:
    return;

  lowest_map[y][x][dnum] = score;

  # Are we there yet?
  if x == endx and y == endy:
    print("Finished with score: " + str(score) + " ; steps=" + str(steps));
    if lowestscore == -1 or score < lowestscore:
      lowestscore = score;

  if lowestscore > -1 and score > lowestscore:
    return;

  # Try step forward
  if d == 'e':
    if map[y][x+1] != '#':
      go(y, x+1, d, score+1, steps+1);
  elif d == 'w':
    if map[y][x-1] != '#':
      go(y, x-1, d, score+1, steps+1);
  elif d == 'n':
    if map[y-1][x] != '#':
      go(y-1, x, d, score+1, steps+1);
  elif d == 's':
    if map[y+1][x] != '#':
      go(y+1, x, d, score+1, steps+1);

  # Try turn CW
  if d == 'e':
    go(y, x, 's', score+1000, steps+1);
  elif d == 's':
    go(y, x, 'w', score+1000, steps+1);
  elif d == 'w':
    go(y, x, 'n', score+1000, steps+1);
  elif d == 'n':
    go(y, x, 'e', score+1000, steps+1);

  # Try turn CCW
  if d == 'w':
    go(y, x, 's', score+1000, steps+1);
  elif d == 'n':
    go(y, x, 'w', score+1000, steps+1);
  elif d == 'e':
    go(y, x, 'n', score+1000, steps+1);
  elif d == 's':
    go(y, x, 'e', score+1000, steps+1);








  
go(starty, startx, 'e', 0, 0);
print("PART A: " + str(lowestscore));
