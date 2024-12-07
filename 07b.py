import copy;
import re;
filename = '07_in.txt';

eqs = []
partb = 0;

with open(filename) as f:
  for l in f:
    line = l.strip()
    result = l.split(':')[0]
    nums = l.split(':')[1].strip().split(' ')
    eq = []
    eq.append(nums);
    eq.append(result);
    eqs.append(eq);


count = 0;
for eq in eqs:
  count += 1;
  print('Doing ' + str(count) + ' of ' + str(len(eqs)));
  can_be_true = 0;
  combos = []
  start = 'x?x'.join(str(item) for item in eq[0]).split('x')
  combos.append(start);
  all_done = 0
  while all_done == 0:
    new_combos = [];
    for c in combos:
      new_add = [];
      new_mul = [];
      new_cat = [];

      first_op = 1;
      for i in c:
        if i == '?' and first_op == 1:
          new_add.append('+');
          new_mul.append('*');
          new_cat.append('||');

          first_op = 0;
        else:
          new_add.append(i);
          new_mul.append(i);
          new_cat.append(i);

      new_combos.append(new_add);
      new_combos.append(new_mul);
      new_combos.append(new_cat);

    combos = copy.deepcopy(new_combos);  
    all_done = 1;
    for n in new_combos:
      if '?' in n:
        all_done = 0;

  for combo in combos:
    c = copy.deepcopy(combo);
    r = int(c.pop(0));
    while len(c) > 1:
      op = c.pop(0);
      num = int(c.pop(0));
      if op == '+':
        r = r + num;
      if op == '*':
        r = r * num;
      if op == '||':
        r = int(str(r) + str(num));
      if r > int(eq[1]):
        break;

    if int(r) == int(eq[1]):
      can_be_true = 1;
      break;

  if can_be_true == 1:
    partb += int(eq[1]);

print("PART B: " + str(partb));

