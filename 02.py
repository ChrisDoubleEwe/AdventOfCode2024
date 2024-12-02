import copy;
filename = '02_in.txt';

reports = [];

with open(filename) as f:
  for l in f:
    line = l.strip()


    rep_str = line.split(' ');
    rep = []
    for r in rep_str:
      rep.append(int(r));
    reports.append(copy.deepcopy(rep));

parta = 0;
partb = 0;

for report in reports:
  increasing = -1;
  decreasing = -1;
  same = -1;
  unsafe_gap = -1;
  last_num = -1;

  for r in report:
    if last_num == -1:
      last_num = r;
      continue;
    
    if r > last_num:
      increasing = 1;
    if r < last_num:
      decreasing = 1;
    if r == last_num:
      same = 1;
    if abs(r - last_num) > 3:
      unsafe_gap = 1;

    last_num = r;

  safe_report = 1;
  if increasing == decreasing:
    safe_report = 0;
  if same == 1:
    safe_report = 0;
  if unsafe_gap == 1:
    safe_report = 0;

  parta += safe_report
  partb += safe_report



  # If unsafe, can we make it safe by removing one item?
  if safe_report == 0:
    made_safe = 0;
    for remove_num in range(0, len(report)):
      this_report = copy.deepcopy(report);
      this_report.pop(remove_num);
      increasing = -1;
      decreasing = -1;
      same = -1;
      unsafe_gap = -1;
      last_num = -1;

      for r in this_report:
        if last_num == -1:
          last_num = r;
          continue;
   
        if r > last_num:
          increasing = 1;
        if r < last_num:
          decreasing = 1;
        if r == last_num:
          same = 1;
        if abs(r - last_num) > 3:
          unsafe_gap = 1;

        last_num = r;

      safe_report = 1;
      if increasing == decreasing:
        safe_report = 0;
      if same == 1:
        safe_report = 0;
      if unsafe_gap == 1:
        safe_report = 0;

      if safe_report == 1:
        made_safe = 1;

    if made_safe == 1:
      partb += 1;

    

print("PART A: " + str(parta));
print("PART B: " + str(partb));




