import copy;
import re;
filename = '05_in.txt';

rules = []
updates = [];
parta = 0;
partb = 0;

do_rules = 1

with open(filename) as f:
  for l in f:
    line = l.strip()

    if line == '':
      do_rules = 0
      continue;

    if do_rules == 1:
      rule = line.split('|')
      new_rule = [];
      new_rule.append(int(rule[0]));
      new_rule.append(int(rule[1]));
      rules.append(new_rule);


    else:
      update = line.split(',')
      new_update = [];
      for u in update:
        new_update.append(int(u));
      updates.append(new_update);


b_updates = [];
for u in updates:
  all_rules_passed = 1;
  for r in rules:
    if r[0] in u:
      if r[1] in u:
        if u.index(r[0]) > u.index(r[1]):
          all_rules_passed = 0;
  if all_rules_passed == 1:
    parta += u[len(u)/2]
  else:
    b_updates.append(u);

print("PARTA: " + str(parta));


for u in b_updates:
  all_rules_passed = 0;
  while all_rules_passed == 0:
    all_rules_passed = 1;
    for r in rules:
      if r[0] in u:
        if r[1] in u:
          idx_a = u.index(r[0]);
          idx_b = u.index(r[1])
          if idx_a > idx_b:
            all_rules_passed = 0;
            u[idx_a] = r[1];
            u[idx_b] = r[0];
  partb += u[len(u)/2]


print("PARTB: " + str(partb));





