import copy;
import re;
filename = '03_in.txt';

input = '';

with open(filename) as f:
  for l in f:
    line = l.strip()
    input += line

p = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
matches = p.findall(input)

parta = 0;

for sum in matches:
  s1 = sum.replace('mul(', '');
  s2 = s1.replace(')', '');
  nums = s2.split(',')
  a = int(nums[0]);
  b = int(nums[1]);
  result = a * b
  parta += result;

print "PART A: " + str(parta);

p = re.compile(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))')
matches = p.findall(input)

partb = 0;

do = 1;
for sum in matches:
  if sum == 'do()':
    do = 1;
    continue;
  if sum == 'don\'t()':
    do = 0;
    continue;
  s1 = sum.replace('mul(', '');
  s2 = s1.replace(')', '');
  nums = s2.split(',')
  a = int(nums[0]);
  b = int(nums[1]);
  result = a * b

  if do == 1:
    partb += result;

print "PART B: " + str(partb);


