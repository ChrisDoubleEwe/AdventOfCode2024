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
      print("GOT GUARD");
      guardx = x;
      guardy = y;
      map[y][x]='X';
      print('x ' + str(guardx) + ' ; y ' + str(guardy));

orig_map = copy.deepcopy(map);
orig_guardx = guardx;
orig_guardy = guardy;
orig_guard_dir = guard_dir;


for x in range(0, len(map[0])):
  for y in range(0, len(map)):

    map = copy.deepcopy(orig_map);
    guardx = orig_guardx;
    guardy = orig_guardy;
    guard_dir = orig_guard_dir;
    # INSERT BLOCKAGE
    if map[y][x] != '.':
      continue;
    print('Insert blockage at x=' + str(x) + ' ; y=' + str(y));
    map[y][x]='#';
    positions = [];
    loop_detected = 0;

    while (guardx >= 0 and guardx < len(map[0]) and guardy >= 0 and guardy < len(map)):
      cur_pos = ':'+str(guardx)+":"+str(guardy)+'++'+str(guard_dir[0])+':'+str(guard_dir[1])+'::';
      if cur_pos in positions:
        print('LOOP DETECTED x=' + str(x) + ' ; y=' + str(y));
        loop_detected = 1;
        break;
      else:
        positions.append(cur_pos);

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

    partb += loop_detected;



print("PART B: " + str(partb));

