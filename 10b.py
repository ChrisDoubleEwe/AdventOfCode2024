import copy;
import sys
import re;
filename = '10_test6.txt';

map = []
empty_map = [];
temp_map = [];
parta = 0;
partb = 0;

with open(filename) as f:
  for l in f:
    line = l.strip()

    row = [-1]
    empty_row = [-1,-1];
    for c in list(line):
      if c == '.':
        row.append(-1);
      else:
        row.append(int(c));
      empty_row.append(-1);
    row.append(-1);
    map.append(copy.deepcopy(row));
    empty_map.append(copy.deepcopy(empty_row));
  temp_map = [];
  temp_map.append(empty_row);
  for r in map:
    temp_map.append(copy.deepcopy(r));
  temp_map.append(empty_row);
  map = copy.deepcopy(temp_map);

  temp_map = [];
  temp_map.append(empty_row);
  for r in empty_map:
    temp_map.append(copy.deepcopy(r));
  temp_map.append(empty_row);
  empty_map = copy.deepcopy(temp_map);




print(map);

zeroes = [];

for y in range(0, len(map)):
  for x in range(0, len(map[0])):
    if map[y][x] == 0:
      pair = [];
      pair.append(x);
      pair.append(y);
      zeroes.append(pair);

print(zeroes);

# Find trails
scores = [];
this_map = copy.deepcopy(empty_map);

print("ZEROES: " + str(zeroes));
for z in zeroes:
  this_map = copy.deepcopy(empty_map);

  this_map[z[1]][z[0]] = 0;

  count = -1;
  while count < 10:
    count += 1

    for y in range(0, len(map)):
      for x in range(0, len(map[0])):
        if this_map[y][x] == count:
          if map[y][x+1] == count+1:
            this_map[y][x+1] = count+1;
          if map[y][x-1] == count+1:
            this_map[y][x-1] = count+1;
          if map[y+1][x] == count+1:
            this_map[y+1][x] = count+1;
          if map[y-1][x] == count+1:
            this_map[y-1][x] = count+1;

  for r in this_map:
    for c in r:
      if c == -1:
        sys.stdout.write('.')
      else:
        sys.stdout.write(str(c))
    print('')

  score = 0;
  for y in range(0, len(map)):
    for x in range(0, len(map[0])):
      if this_map[y][x] == 9:
        score += 1;

  scores.append(score);

print(scores);
  
for s in scores:
  parta += s;

print("PART A: " + str(parta));

# Calculate ratings

def calc_rat_step(rating, step, x, y):
  print("Entering calc_rat_step with: " + str(rating) + " ; " + str(step) + " ; " + str(x) + " ; " + str(y));
  if step == 9:
    return rating;
  count_choices = 0;
  if map[y][x+1] == step+1:
    count_choices += 1;
  if map[y][x-1] == step+1:
    count_choices += 1;
  if map[y+1][x] == step+1:
    count_choices += 1;
  if map[y-1][x] == step+1:
    count_choices += 1;
  print("rating: " + str(rating));
  print("count_choices: " + str(count_choices));

  rating = rating * count_choices;
  if map[y][x+1] == step+1:
    print("rCalling calc_rat_step with: " + str(rating) + " ; " + str(step+1) + " ; " + str(x+1) + " ; " + str(y));
    rating = calc_rat_step(rating, step+1, x+1, y)
  if map[y][x-1] == step+1:
    print("lCalling calc_rat_step with: " + str(rating) + " ; " + str(step+1) + " ; " + str(x-1) + " ; " + str(y));
    rating = calc_rat_step(rating, step+1, x-1, y)
  if map[y+1][x] == step+1:
    print("dCalling calc_rat_step with: " + str(rating) + " ; " + str(step+1) + " ; " + str(x) + " ; " + str(y+1));
    rating = calc_rat_step(rating, step+1, x, y+1)
  if map[y-1][x] == step+1:
    print("uCalling calc_rat_step with: " + str(rating) + " ; " + str(step+1) + " ; " + str(x) + " ; " + str(y-1));
    rating = calc_rat_step(rating, step+1, x, y-1)




for z in zeroes:
  print("ZERO :" + str(z));
  rating = calc_rat_step(1, 0, z[0], z[1])
  print("RATING: " + str(rating));
