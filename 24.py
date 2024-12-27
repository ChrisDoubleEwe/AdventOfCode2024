import copy;
import itertools
import os;
import sys
import math;
sys.setrecursionlimit(10000)
import re;
filename = '24_in.txt';

parta = 0;
partb = 0;
signals = {}
gates = []
all_signals = [];
z_signals = [];
x_signals = [];
y_signals = [];



br = 0;
with open(filename) as f:
  for line in f:
    if line.strip() == '':
      br = 1;
      continue;
    l = line.strip();
    if br == 0:
      wire = l.split(': ')[0];
      value = l.split(': ')[1];
      signals[wire] = int(value);
      all_signals.append(wire);
    else:
      in1 = l.split(' ')[0];
      in2 = l.split(' ')[2];
      op = l.split(' ')[1];
      out = l.split(' ')[4];
      triple = [];
      triple.append(in1);
      triple.append(in2);
      triple.append(op);
      triple.append(out);
      gates.append(copy.deepcopy(triple));
      if in1 not in all_signals:
        all_signals.append(in1);
        signals[in1] = -1;
      if in2 not in all_signals:
        all_signals.append(in2);
        signals[in2] = -1;
      if out not in all_signals:
        all_signals.append(out);
        signals[out] = -1;


for s in signals:
  if s.startswith('z'):
    z_signals.append(s);
  if s.startswith('x'):
    x_signals.append(s);
  if s.startswith('y'):
    y_signals.append(s);



# SET TEST VALUES
#for s in signals:
#  if s.startswith('x'):
#    signals[s] = 0;
#  if s.startswith('y'):
#    signals[s] = 0;

#signals['x01'] = 1;



sorted_z = sorted(z_signals)


not_all_done = 0;
while not_all_done == 0:
  not_all_done = 1
  for s in signals:
    if signals[s] == -1:
      not_all_done = 0;

  for g in gates:
    if signals[g[0]] != -1 and signals[g[1]] != -1:
      if g[2] == 'OR':
        if signals[g[0]] == 1 or signals[g[1]] == 1:
          signals[g[3]] = 1;
        else:
          signals[g[3]] = 0;
      if g[2] == 'AND':
        if signals[g[0]] == 1 and signals[g[1]] == 1:
          signals[g[3]] = 1;
        else:
          signals[g[3]] = 0;
      if g[2] == 'XOR':
        if signals[g[0]] != signals[g[1]]:
          signals[g[3]] = 1;
        else:
          signals[g[3]] = 0;


  
sorted_z.reverse();

bin_result = '';
for z in sorted_z:
  bin_result += str(signals[z]);
parta = int(bin_result, 2)
print("PART A: " + str(parta));

