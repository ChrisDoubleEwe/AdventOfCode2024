parta = 0;
filename = '01_in.txt';

with open(filename) as f:
  for l in f:
    line = l.strip()

    print line;

print("PART A: " + str(parta));

