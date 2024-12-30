import copy;
from random import randint, choice

import itertools
import os;
import sys
import math;
sys.setrecursionlimit(10000)
import re;
filename = '24_in.txt';

parta = 0;
signals = {}
gates = []
all_signals = [];
z_signals = [];
x_signals = [];
y_signals = [];
swaps = [];
output_pins = []



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
      output_pins.append(out);
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

for s in signals:
  if s not in z_signals and s not in x_signals and s not in y_signals:
    swaps.append(s);


sorted_z = sorted(z_signals)
sorted_x = sorted(x_signals)
sorted_y = sorted(y_signals)
sorted_z.reverse();
sorted_x.reverse();
sorted_y.reverse();




def test(changed_pin):
  global signals;
  global gates;
  wrong_count = 0;

  not_all_done = 0;
  loop_count = 0;
  while not_all_done == 0:
    loop_count += 1;
    if loop_count > 100:
      return(99);

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

  z_bin_result = '';
  for z in sorted_z:
    z_bin_result += str(signals[z]);
  z_result = int(z_bin_result, 2)

  x_bin_result = '';
  for x in sorted_x:
    x_bin_result += str(signals[x]);
  x_result = int(x_bin_result, 2)

  y_bin_result = '';
  for y in sorted_y:
    y_bin_result += str(signals[y]);
  y_result = int(y_bin_result, 2)

  #print(x_bin_result)
  #print("+");
  #print(y_bin_result)
  #print("=");
  #print(z_bin_result)



  if z_result != x_result + y_result:
    #print("WRONG   RESULT when x" + changed_pin + " set to " + str(signals['x'+changed_pin]) + " and y" + changed_pin + " set to " + str(signals['y'+changed_pin]) + ": " + str(z_bin_result));

    #print("WRONG RESULT when " + changed_pin + " set to 1: " + str(x_result) + " + " + str(y_result) + " = " + str(z_result) + " -- " + str(len(z_bin_result) - z_bin_result.index('1') - 1));
    wrong_count += 1;
  #else:
  #  print("CORRECT RESULT when x" + changed_pin + " set to " + str(signals['x'+changed_pin]) + " and y" + changed_pin + " set to " + str(signals['y'+changed_pin]) + ": " + str(z_bin_result));

  return wrong_count;

def test_all():
  global signals;
  global gates;
  # SET TEST VALUES
  for s in signals:
    if s.startswith('x'):
      signals[s] = 0;
    elif s.startswith('y'):
      signals[s] = 0;
    else:
      signals[s] = -1;


  wrong_count = 0;
  for i in range(0,45):
    for this_x_val in range(0, 2):
      for this_y_val in range(0, 2):
        for other_x_val in range(0, 2):
          for other_y_val in range(0, 2):
            if wrong_count > 0:
              return(wrong_count);
            for s in signals:
              if s.startswith('x'):
                signals[s] = 0;
              elif s.startswith('y'):
                signals[s] = 0;
              else:
                signals[s] = -1;

            i_str = str(i).zfill(2);
            x_pin = 'x' + i_str;
            y_pin = 'y' + i_str;
            z_pin = 'z' + i_str;
            for z in range(0,45):
              z_str = str(z).zfill(2);
              x_zpin = 'x' + z_str;
              y_zpin = 'y' + z_str;
              z_zpin = 'z' + z_str;
              if z == i:
                signals[x_zpin] = this_x_val;
                signals[y_zpin] = this_y_val;
              else:
                signals[x_zpin] = other_x_val;
                signals[y_zpin] = other_y_val;
            wrong_count += test(i_str);

  return(wrong_count);



test_all();
orig_gates = copy.deepcopy(gates);
#swap_pairs = [['fvw', 'z18'], ['mdb', 'z22'], ['nwq', 'z36'], ['rpv', 'grf']] 
swap_pairs = [['fvw', 'z18'], ['mdb', 'z22'], ['nwq', 'z36'], ['wpq', 'grf']]


gates = copy.deepcopy(orig_gates);

pin_list = [];
for s in swap_pairs:
  pin_list.append(s[0]);
  pin_list.append(s[1]);

  print("Swap " + s[0] + " with " + s[1]);

  for g in range(0, len(gates)):
    if gates[g][3] == s[0]:
      gates[g][3] = s[1];
    elif gates[g][3] == s[1]:
      gates[g][3] = s[0];

sorted_pin_list = sorted(pin_list);
print(sorted_pin_list);
partb = ','.join(sorted_pin_list);

res = test_all();
print('');
print("Number of errors: " + str(res));
print('');
print("PART B: ");
print(partb)
exit();


print("TRYING TO FIND grf SWAP PIN");

orig_gates = copy.deepcopy(gates);

xcount = 0
for y in ['grf']:
 for x in output_pins:
  xcount += 1
  gates = copy.deepcopy(orig_gates);

  print("Trying " + x + " and " + y + " (" + str(xcount) + " / " + str(len(output_pins)) + " )" );
  for g in range(0, len(gates)):
    if gates[g][3] == y:
      gates[g][3] = x;
    elif gates[g][3] == x:
      gates[g][3] = y;

  res = test_all();
  print(res);
  if res == 0:
    exit();





