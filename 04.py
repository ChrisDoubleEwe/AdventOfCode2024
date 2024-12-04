import copy;
import re;
filename = '04_in.txt';

map = []
blankrow = [];
parta = 0;
partb = 0;

with open(filename) as f:
  for l in f:
    line = l.strip()
    row = list(line);
    newrow = ['.','.','.'];
    for i in row:
      newrow.append(i);
    newrow.append('.');
    newrow.append('.');
    newrow.append('.');



    map.append(copy.deepcopy(newrow));
for z in range(0, len(map[0])):
  blankrow.append('.');

map.append(copy.deepcopy(blankrow));
map.append(copy.deepcopy(blankrow));
map.append(copy.deepcopy(blankrow));
map.insert(0, copy.deepcopy(blankrow))
map.insert(0, copy.deepcopy(blankrow))
map.insert(0, copy.deepcopy(blankrow))






for y in range(0, len(map)):
  for x in range(0, len(map[0])):
    # RIGHT
    if map[y][x] == 'X' and map[y][x+1] == 'M' and map[y][x+2] == 'A' and map[y][x+3] == 'S':
      parta += 1
    # LEFT
    if map[y][x] == 'X' and map[y][x-1] == 'M' and map[y][x-2] == 'A' and map[y][x-3] == 'S':
      parta += 1
    # DOWN
    if map[y][x] == 'X' and map[y+1][x] == 'M' and map[y+2][x] == 'A' and map[y+3][x] == 'S':
      parta += 1
    # UP
    if map[y][x] == 'X' and map[y-1][x] == 'M' and map[y-2][x] == 'A' and map[y-3][x] == 'S':
      parta += 1
    # DIAG-RIGHT-UP
    if map[y][x] == 'X' and map[y-1][x+1] == 'M' and map[y-2][x+2] == 'A' and map[y-3][x+3] == 'S':
      parta += 1
    # DIAG-RIGHT-DOWN
    if map[y][x] == 'X' and map[y+1][x+1] == 'M' and map[y+2][x+2] == 'A' and map[y+3][x+3] == 'S':
      parta += 1
    # DIAG-LEFT-UP
    if map[y][x] == 'X' and map[y-1][x-1] == 'M' and map[y-2][x-2] == 'A' and map[y-3][x-3] == 'S':
      parta += 1
    # DIAG-LEFT-DOWN
    if map[y][x] == 'X' and map[y+1][x-1] == 'M' and map[y+2][x-2] == 'A' and map[y+3][x-3] == 'S':
      parta += 1



    # M S
    #  A
    # M S
    if map[y][x] == 'A' and map[y-1][x-1] == 'M' and map[y+1][x+1] == 'S':
      if map[y+1][x-1] == 'M' and map[y-1][x+1] == 'S':
        partb += 1  


    # M M
    #  A
    # S S
    if map[y][x] == 'A' and map[y-1][x-1] == 'M' and map[y+1][x+1] == 'S':
      if map[y+1][x-1] == 'S' and map[y-1][x+1] == 'M':
        partb += 1


    # S S
    #  A
    # M M
    if map[y][x] == 'A' and map[y-1][x-1] == 'S' and map[y+1][x+1] == 'M':
      if map[y+1][x-1] == 'M' and map[y-1][x+1] == 'S':
        partb += 1



    # S M
    #  A
    # S M
    if map[y][x] == 'A' and map[y-1][x-1] == 'S' and map[y+1][x+1] == 'M':
      if map[y+1][x-1] == 'S' and map[y-1][x+1] == 'M':
        partb += 1



print("PARTA: " + str(parta));
print("PARTB: " + str(partb));



