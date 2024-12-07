import copy;
import re;
filename = '06_in.txt';

map = []
parta = 0;
partb = 0;

guardx = 0;
guardy = 0;
guard_dir = [0,-1];


with open(filename) as f:
  for l in f:
    line = l.strip()

    map.append(list(line));

for x in range(0, len(map[0])):
  for y in range(0, len(map)):
    if map[y][x] == '^':
      guardx = x;
      guardy = y;
      map[y][x]='X';


while (guardx >= 0 and guardx < len(map[0]) and guardy >= 0 and guardy < len(map)):
  newguardy = guardy + guard_dir[1];
  newguardx = guardx + guard_dir[0];
  if (newguardx < 0 or newguardx > len(map[0])-1 or newguardy < 0 or newguardy > len(map)-1):
    break;
  if map[guardy + guard_dir[1]][guardx + guard_dir[0]] != '#':
    guardy = guardy + guard_dir[1];
    guardx = guardx + guard_dir[0];
    if (guardx < 0 or guardx > len(map[0])-1 or guardy < 0 or guardy > len(map)-1):
      break;
    map[guardy][guardx] = 'X';
  else:
    if guard_dir == [0,-1]:
      guard_dir = [1,0];
    elif guard_dir == [1,0]:
      guard_dir = [0,1];
    elif guard_dir == [0,1]:
      guard_dir = [-1,0];
    elif guard_dir == [-1,0]:
      guard_dir = [0,-1];




row = '';
for y in range(0, len(map)):
  row = '';
  for x in range(0, len(map[0])):
    row += map[y][x];
    if map[y][x] == 'X':
      parta += 1;


print("PART A: " + str(parta));

