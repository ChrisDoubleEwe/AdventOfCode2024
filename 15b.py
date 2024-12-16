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
        if c == '#':
          row.append('#');
          row.append('#');
        if c == 'O':
          row.append('[');
          row.append(']');
        if c == '.':
          row.append('.');
          row.append('.');
        if c == '@':
          row.append('@');
          row.append('.');

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

print(x)
print(y)

for i in instr:
  print(' ');
  print("Move: " + str(i))

  if i == '<':
    if map[y][x-1] == '.':
      map[y][x] = '.';
      x = x-1;
      map[y][x] = '@';
    else:
      if map[y][x-1] == ']':
        inc = 0;
        hit_wall = 0;
        hit_space = 0;
        while hit_wall == 0 and hit_space == 0:
          inc+=1;
          if map[y][x-1-inc] == '.':
            hit_space = 1;
            map[y][x-1-inc] = '[';
            for i in range(0, inc):
              if map[y][x-1-i] == '[':
                map[y][x-1-i] = ']';
              else:
                map[y][x-1-i] = '[';
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
      if map[y][x+1] == '[':
        inc = 0;
        hit_wall = 0;
        hit_space = 0;
        while hit_wall == 0 and hit_space == 0:
          inc+=1;
          if map[y][x+1+inc] == '.':
            hit_space = 1;
            map[y][x+1+inc] = ']';
            for i in range(0, inc):
              if map[y][x+1+i] == '[':
                map[y][x+1+i] = ']';
              else:
                map[y][x+1+i] = '[';
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
      if map[y-1][x] == '[' or map[y-1][x] == ']':
        print("here");
        boxes = [];
        pair = [];
        if map[y-1][x] == '[':
          pair.append(y-1);
          pair.append(x);
        else:
          pair.append(y-1);
          pair.append(x-1);
        boxes.append(copy.deepcopy(pair));
        last = -1;
        while len(boxes) > last:
          print(boxes);
          last = len(boxes);
          for b in boxes:
            if map[b[0]-1][b[1]] == '[' or map[b[0]-1][b[1]] == ']':
              p = [];
              if map[b[0]-1][b[1]] == '[':
                p.append(b[0]-1);
                p.append(b[1]);
              else:
                p.append(b[0]-1);
                p.append(b[1]-1);
              if p not in boxes:
                boxes.append(copy.deepcopy(p));
            if map[b[0]-1][b[1]+1] == '[' or map[b[0]-1][b[1]+1] == ']':
              p = [];
              if map[b[0]-1][b[1]+1] == '[':
                p.append(b[0]-1);
                p.append(b[1]+1);
              else:
                p.append(b[0]-1);
                p.append(b[1]);
              if p not in boxes:
                boxes.append(copy.deepcopy(p));
        can_move = 1;
        for b in boxes:
          if map[b[0]-1][b[1]] == '#' or map[b[0]-1][b[1]+1] == '#':
            can_move = 0;
        if can_move == 1: 
          for b in boxes:
            map[b[0]][b[1]] = '.';
            map[b[0]][b[1]+1] = '.';
          for b in boxes:
            map[b[0]-1][b[1]] = '[';
            map[b[0]-1][b[1]+1] = ']';
          map[y][x] = '.';
          y = y-1;
          map[y][x] = '@';



              
  if i == 'v':
    if map[y+1][x] == '.':
      map[y][x] = '.';
      y = y+1;
      map[y][x] = '@';
    else:
      if map[y+1][x] == '[' or map[y+1][x] == ']':
        print("here");
        boxes = [];
        pair = [];
        if map[y+1][x] == '[':
          pair.append(y+1);
          pair.append(x);
        else:
          pair.append(y+1);
          pair.append(x-1);
        boxes.append(copy.deepcopy(pair));
        last = -1;
        while len(boxes) > last:
          print(boxes);
          last = len(boxes);
          for b in boxes:
            if map[b[0]+1][b[1]] == '[' or map[b[0]+1][b[1]] == ']':
              p = [];
              if map[b[0]+1][b[1]] == '[':
                p.append(b[0]+1);
                p.append(b[1]);
              else:
                p.append(b[0]+1);
                p.append(b[1]-1);
              if p not in boxes:
                boxes.append(copy.deepcopy(p));
            if map[b[0]+1][b[1]+1] == '[' or map[b[0]+1][b[1]+1] == ']':
              p = [];
              if map[b[0]+1][b[1]+1] == '[':
                p.append(b[0]+1);
                p.append(b[1]+1);
              else:
                p.append(b[0]+1);
                p.append(b[1]);
              if p not in boxes:
                boxes.append(copy.deepcopy(p));
        can_move = 1;
        for b in boxes:
          if map[b[0]+1][b[1]] == '#' or map[b[0]+1][b[1]+1] == '#':
            can_move = 0;
        if can_move == 1:
          for b in boxes:
            map[b[0]][b[1]] = '.';
            map[b[0]][b[1]+1] = '.';
          for b in boxes:
            map[b[0]+1][b[1]] = '[';
            map[b[0]+1][b[1]+1] = ']';
          map[y][x] = '.';
          y = y+1;
          map[y][x] = '@';

    

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
    if c == '[':
      print(str((100*this_y)+this_x));
      parta += (100 * this_y);
      parta += this_x;

print("PART B: " + str(parta));
