import sys
import time

title = "## Day 23: Coprocessor Conflagration ##"
url = "https://adventofcode.com/2017/day/23"
expectedResultPart1 = 6724
expectedResultPart2 = 903

class Instruction:
    def __init__(self, op, x, x_mode, y=None, y_mode=True):
        self.op = op
        self.x = x
        self.x_mode = x_mode
        self.y = y
        self.y_mode = y_mode

    def state(self):
        return f"op:{self.op}, x:{self.x}, y:{self.y}"

def partOne(input):
    registers = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0}
    
    instructions = get_instruction_set(input)
    ip = 0
    mul_count = 0
    while ip >= 0 and ip < len(instructions):
        ins = instructions[ip]
        ip += executePartOne(ins, registers)
        if ins.op == 'mul':
            mul_count += 1

    return mul_count


def partTwo(input):
    register_h = optimized_program()
    return register_h

# optimizations commented
# assume only allowed to use available operators. Ie. not modulo
def optimized_program():
    a = 1
    b = 108400
    c = 125400
    h = 0
    while c >= b:
        multiple_found = False
        a = 0
        f = 1
        d = 2
        while d < 354: # d will never be larger than the sqrt of c (125400)
            # start e from d rather than 2 on each iteration
            e = d
            while b > e:
                if b == (d * e):
                    f = 0
                    # add a jump stright to h increment when a factor is found
                    multiple_found = True
                    break
                e += 1
            if multiple_found:
                break
            # make use of the unused a register to increment in 2s after d reaches 3
            d += 1 + a
            a = 1
        if f == 0:
            h += 1

        b += 17
    return h


def executePartOne(ins, registers):
    if ins.op == 'set':
        registers[ins.x] = get_value(ins.y, ins.y_mode, registers)
    elif ins.op == 'sub':
        registers[ins.x] -= get_value(ins.y, ins.y_mode, registers)
    elif ins.op == 'mul':
        registers[ins.x] *= get_value(ins.y, ins.y_mode, registers)
    elif ins.op == 'jnz':
        x = get_value(ins.x, ins.x_mode, registers)
        if x != 0:
            return get_value(ins.y, ins.y_mode, registers)
    else:
        assert False, f"Unknown instruction: {ins}"

    return 1

def get_value(val, mode, registers):
    return val if mode else registers[val]

def is_numeric(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def get_instruction_set(input):
    instructions = []
    lines = input.splitlines()
    for line in lines:
        op = line[:3]
        operands = line[4:].split(' ')
        x = operands[0]
        x_mode = False
        if is_numeric(x):
            x_mode = True
            x = int(x)
        y = None
        y_mode = False
        if (len(operands) == 2):
            y = operands[1]
            if is_numeric(y):
                y_mode = True
                y = int(y)
        instructions.append(Instruction(op, x, x_mode, y, y_mode))
    return instructions

print(title)
print(url)
for filePath in sys.argv[1:]:
    print(f"\nFile: {filePath}")
    with open(filePath, 'r') as file:
        input = file.read()

    start = time.perf_counter()
    resultPartOne = partOne(input);
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Part 1 Result: {resultPartOne} in {elapsed_ms:.3f}ms");

    start = time.perf_counter()
    resultPartTwo = partTwo(input);
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Part 2 Result: {resultPartTwo} in {elapsed_ms:.3f}ms");

if (resultPartOne != expectedResultPart1 or resultPartTwo != expectedResultPart2):
        sys.exit(1)
