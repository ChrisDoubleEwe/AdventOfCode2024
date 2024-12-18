import copy;
import sys
import math;
sys.setrecursionlimit(10000)
import re;
filename = '17_in.txt';

parta = 0;
partb = 0;

prog = [];
reg_a = 0;
reg_b = 0;
reg_c = 0;

output = '';


with open(filename) as f:
  for line in f:
    l = line.strip()
    if "Register A: " in l:
      reg_a = int(l.split(':')[1].strip())
    if "Register B: " in l: 
      reg_b = int(l.split(':')[1].strip())
    if "Register C: " in l:
      reg_c = int(l.split(':')[1].strip())
    if "Program: " in l:
      p = l.split(':')[1].strip().split(',');
      for z in p:
        prog.append(int(z));

print(reg_a);
print(reg_b);
print(reg_c);
print(prog);

def combo(o):
  global reg_a;
  global reg_b;
  global reg_c;

  if o == 0:
    return 0;
  if o == 1:
    return 1;
  if o == 2:
    return 2;
  if o == 3:
    return 3;
  if o == 4:
    return reg_a;
  if o == 5:
    return reg_b;
  if o == 6:
    return reg_c;




pc = 0;
while pc <= len(prog)-2:
  print('------');
  instr = prog[pc];
  pc += 1;
  op = prog[pc];
  pc += 1;

  res = 0;

  new_pc = pc;

  # 0 : ADV divide to A
  # The adv instruction (opcode 0) performs division. The numerator is the value in
  # the A register. The denominator is found by raising 2 to the power of the
  # instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2);
  # an operand of 5 would divide A by 2^B.) The result of the division operation is
  # truncated to an integer and then written to the A register.

  if instr == 0:
    numerator = reg_a;
    denominator = pow(2, combo(op));
    res = math.trunc(numerator / denominator);
    reg_a = res;

  # 1 : BXL bitwise XOR B ^ op
  # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and
  # the instruction's literal operand, then stores the result in register B.

  if instr == 1:
    res = reg_b ^ op;
    reg_b = res;

  # 2 : BST mod 8
  # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8
  # (thereby keeping only its lowest 3 bits), then writes that value to the B register.
  if instr == 2:
    res = combo(op) % 8;
    reg_b = res;

  # 3 : JNZ jump if not zero
  # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if
  # the A register is not zero, it jumps by setting the instruction pointer to the
  # value of its literal operand; if this instruction jumps, the instruction pointer
  # is not increased by 2 after this instruction.

  if instr == 3:
    if reg_a != 0:
      new_pc = op;


  # 4 : BCX bitwise XOR B ^ C
  # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and
  # register C, then stores the result in register B. (For legacy reasons, this
  # instruction reads an operand but ignores it.)

  if instr == 4:
    res = reg_b ^ reg_c;
    reg_b = res;


  # 5 : OUT output
  # The out instruction (opcode 5) calculates the value of its combo operand
  # modulo 8, then outputs that value. (If a program outputs multiple values,
  # they are separated by commas.)

  if instr == 5:
    res = combo(op) % 8;
    output+=str(res);
    output += ','


  # 6 : BDV divide to B
  # The bdv instruction (opcode 6) works exactly like the adv instruction except
  # that the result is stored in the B register. (The numerator is still read from
  # the A register.)

  if instr == 6:
    numerator = reg_a;
    denominator = pow(2, combo(op));
    res = math.trunc(numerator / denominator);
    reg_b = res;


  # 6 : CDV divide to C
  # The cdv instruction (opcode 7) works exactly like the adv instruction except
  # that the result is stored in the C register. (The numerator is still read
  # from the A register.)

  if instr == 7:
    numerator = reg_a;
    denominator = pow(2, combo(op));
    res = math.trunc(numerator / denominator);
    reg_c = res;




  pc = new_pc;


    

   
  print("---------------------");
  print("PC: " + str(pc));
  print("INSTR: " + str(instr) + " " + str(op));
  print("A: " + str(reg_a));
  print("B: " + str(reg_b));
  print("C: " + str(reg_c));

output = output[:-1]
print(output);

