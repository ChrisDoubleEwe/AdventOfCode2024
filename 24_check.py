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
partb = 0;
signals = {}
gates = []
all_signals = [];
z_signals = [];
x_signals = [];
y_signals = [];
swaps = [];



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

  if z_result != x_result + y_result:
    print("WRONG   RESULT when x" + changed_pin + " set to " + str(signals['x'+changed_pin]) + " and y" + changed_pin + " set to " + str(signals['y'+changed_pin]) + ": " + str(z_bin_result));

    #print("WRONG RESULT when " + changed_pin + " set to 1: " + str(x_result) + " + " + str(y_result) + " = " + str(z_result) + " -- " + str(len(z_bin_result) - z_bin_result.index('1') - 1));
    wrong_count += 1;
  else:
    print("CORRECT RESULT when x" + changed_pin + " set to " + str(signals['x'+changed_pin]) + " and y" + changed_pin + " set to " + str(signals['y'+changed_pin]) + ": " + str(z_bin_result));

  return wrong_count;

def check_all():
  for i in range(1, 45):
    x1 = [];
    x2 = [];

    i_str = str(i).zfill(2);
    x_pin = 'x' + i_str;
    y_pin = 'y' + i_str;
    z_pin = 'z' + i_str;

    for g in gates:
      if (g[0] == x_pin or g[1] == x_pin) and g[2] == 'AND':
        a1 = copy.deepcopy(g)
    for g in gates:
      if (g[0] == x_pin or g[1] == x_pin) and g[2] == 'XOR':
        x1 = copy.deepcopy(g)
    for g in gates:
      if (g[0] == x1[3] or g[1] == x1[3]) and g[2] == 'XOR':
        x2 = copy.deepcopy(g)



    for g in gates:
      if g[0] == a1[3] or g[1] == a1[3]:
        o1 = copy.deepcopy(g)

    print(str(i) + str(x1) + ' -> ' + str(x2) );
 
 

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
        signals[x_zpin] = 1;
        signals[y_zpin] = 1;
      else:
        signals[x_zpin] = 1;
        signals[y_zpin] = 1;
    wrong_count += test(i_str);


  return(wrong_count);
check_all();
exit();


#swaps = ['svb', 'fsw', 'nwq', 'hsh', 'pjd', 'bsk', 'tmt', 'dbj', 'qcv', 'fvw', 'ndj', 'bms', 'cpt', 'wcj', 'nct', 'msm', 'thq', 'bmg', 'nfh', 'cjb', 'kqr', 'mtd', 'pcq', 'fvv', 'vmj', 'vsm', 'nqs', 'psj', 'rqp', 'gnt', 'jrk', 'nhq', 'vjj', 'dqq', 'gkj', 'ntg', 'hjc', 'bff', 'mvd', 'gdw', 'bqc', 'mdd', 'dsm', 'qmh', 'cbs', 'pfr', 'sbd', 'ddf', 'pvc', 'shr', 'rpv', 'wpq', 'wjv', 'dtt', 'qgt', 'jdw', 'pvd', 'ctn', 'jvp', 'smc', 'rrt', 'fqs', 'nwg', 'fsf', 'mdb', 'mqc', 'sjg', 'kjd', 'dwf', 'rww', 'mcw', 'mkq', 'vmf', 'fgg', 'fdq', 'phs', 'gsc', 'hrn', 'kvn', 'rjn', 'svf', 'jqn', 'rwg', 'rqd', 'knv', 'dnn', 'hrd', 'nwp', 'btd', 'bqv', 'dtp', 'skg', 'dmf', 'nhj', 'spm', 'vmq', 'hmw', 'dwq', 'tkd', 'jjg', 'hwd', 'npn', 'jpq', 'wjg', 'rjb', 'kwm', 'gfc', 'wfh', 'ppj', 'jrp', 'ckm', 'vds', 'grf', 'hgj', 'chd', 'prv', 'jqg', 'dhg', 'tpj', 'pws', 'bjg', 'rrr', 'vbm', 'hsj', 'ffh', 'gjb', 'djh', 'jqj', 'hgq', 'fbm', 'rmj', 'cbr', 'vrp', 'smh', 'whh', 'qcq', 'kjq', 'fmd', 'gcw', 'jpb', 'sbs', 'dqr', 'rnw', 'wjp', 'vdd', 'qjc', 'fdk', 'kvm', 'krc', 'hwk', 'bqk', 'fbd', 'ftr', 'fkw', 'bcc', 'mhf', 'dcn', 'wpr', 'rtt', 'wmg', 'bnv', 'vvt', 'htp', 'tvh', 'qvr', 'nrr', 'vvb', 'bct', 'tdg', 'tvb', 'gbn', 'bfv', 'rvn', 'nqg', 'gpc', 'pfb']
# swaps = ['fvw', 'cjb', 'kqr', 'ndj', 'gdw', 'ffh', 'vvt', 'bct', 'wpq', 'rqd', 'wpq', 'grf']

# pins z05 and z06 are swapped
#swaps = ['wpq', 'rqd']
# pins z18 and z19 are swapped
#swaps = ['cjb', 'ndj']
# pins z17 and z18 are swapped
#swaps = ['kqr', 'fvw']

print(swaps);

orig_gates = copy.deepcopy(gates);
for s1 in swaps:
  for s2 in swaps:
    if s1 == s2:
      continue;
    print("SWAP " + s1 + " with " + s2);

    gates = copy.deepcopy(orig_gates);
    for g in range(0, len(gates)):
      if gates[g][3] == s1:
        gates[g][3] = s2;
      elif gates[g][3] == s2:
        gates[g][3] = s1;



    res = test_all();
    print("Swapping " + s1 + " with " + s2 + " gives: " + str(res));
exit();

swap_pairs = [['wpq', 'rqd'], ['cjb', 'ndj'], ['kqr', 'fvw']] 
# fvw cjb 
# fvw kqr
# ndj cjb
# cjb gdw
# cjb ffh
# cjb vvt
# cjb bct
# wpq rqd
# wpq grf
#Swapping fvw with cjb gives: 4
#Swapping cjb with fvw gives: 4
#Swapping cjb with ffh gives: 4
#Swapping cjb with vvt gives: 4
#Swapping ffh with cjb gives: 4
#Swapping vvt with cjb gives: 4


print("SWAPPING");
gates = copy.deepcopy(orig_gates);

for s in swap_pairs:
  print(s[0]);
  print(s[1]);

  for g in range(0, len(gates)):
    if gates[g][3] == s[0]:
      gates[g][3] = s[1];
    elif gates[g][3] == s[1]:
      gates[g][3] = s[0];

res = test_all();
print(res);





