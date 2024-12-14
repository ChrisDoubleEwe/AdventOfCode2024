from fractions import gcd
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
      pair.append(int(x)+10000000000000);
      pair.append(int(y)+10000000000000);
      machine.append(copy.deepcopy(pair));
    if line == '':
      machines.append(copy.deepcopy(machine));
      machine = [];

for m in machines:
  cheapest = -1;

  a_presses = (m[2][0]*m[1][1] - m[2][1]*m[1][0]) / (m[0][0]*m[1][1] - m[0][1]*m[1][0])
  b_presses = (m[2][1]*m[0][0] - m[2][0]*m[0][1]) / (m[0][0]*m[1][1] - m[0][1]*m[1][0])

  if a_presses == int(a_presses) and b_presses == int(b_presses):
    cheapest = (3*int(a_presses))+int(b_presses);
  if cheapest == -1:
    #print("NO WIN");
    dummy=1;
  else:
    partb += cheapest;

print("PART B: " + str(partb));

