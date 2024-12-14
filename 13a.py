import copy;
import sys
import re;
filename = '13_in.txt';


map = []
parta = 0;
partb = 0;
crops = [];

machines = [];
machine = [];


with open(filename) as f:
  for l in f:
    line = l.strip()
    if "Button A" in line:
      s = line.split(': ')[1];
      s1 = s.split(', ');
      x = s1[0].split('+')[1];
      y = s1[1].split('+')[1];
      pair = [];
      pair.append(int(x));
      pair.append(int(y));
      machine.append(copy.deepcopy(pair));
    if "Button B" in line:
      s = line.split(': ')[1];
      s1 = s.split(', ');
      x = s1[0].split('+')[1];
      y = s1[1].split('+')[1];
      pair = [];
      pair.append(int(x));
      pair.append(int(y));
      machine.append(copy.deepcopy(pair));
    if "Prize" in line:
      s = line.split(': ')[1];
      s1 = s.split(', ');
      x = s1[0].split('=')[1];
      y = s1[1].split('=')[1];
      pair = [];
      pair.append(int(x));
      pair.append(int(y));
      machine.append(copy.deepcopy(pair));
    if line == '':
      machines.append(copy.deepcopy(machine));
      machine = [];

for m in machines:
  cheapest = 9999;
  for a_presses in range(0,101):
    for b_presses in range(0,101):
      if (m[0][0]*a_presses)+(m[1][0]*b_presses) == m[2][0]:
        if (m[0][1]*a_presses)+(m[1][1]*b_presses) == m[2][1]:
          if (3*a_presses)+b_presses < cheapest:
            cheapest = (3*a_presses)+b_presses;
  if cheapest >= 999:
    dummy=1
  else:
    parta += cheapest;

print("PART A: " + str(parta));

