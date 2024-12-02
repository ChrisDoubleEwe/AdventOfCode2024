filename = '01_in.txt';
left = [];
right = [];

with open(filename) as f:
  for l in f:
    line = l.strip()
    left.append(int(line.split('   ')[0]));
    right.append(int(line.split('   ')[1]));

left.sort();
right.sort();

diff = 0;
for i in range(0, len(left)):
   diff += abs(left[i] - right[i])

print("PART A: " + str(diff));



partb = 0
for i in range(0, len(left)):
  num = left[i];
  count = 0;
  for j in range(0, len(left)):
    if right[j] == num:
      count += 1;
  partb += num * count;

print("PART B: " + str(partb));





