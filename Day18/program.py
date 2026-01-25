import sys
import time
import queue

title = "## Day 18: Duet ##"
url = "https://adventofcode.com/2017/day/18"
expectedResultPart1 = 2951
expectedResultPart2 = 7366

class Instruction:
    def __init__(self, op, x, x_mode, y=None, y_mode=True):
        self.op = op
        self.x = x
        self.x_mode = x_mode
        self.y = y
        self.y_mode = y_mode

def partOne(input):
    registers = {}
    instructions = get_instruction_set(input)
    initialize_register(registers, instructions, 0)
    ip = 0
    while ip < len(instructions):
        ins = instructions[ip]
        ip += executePartOne(ins, registers)
        if ins.op == 'rcv' and 'rcv' in registers:
            return registers['rcv']
    return -1

def partTwo(input):
    registers0 = {}
    registers1 = {}
    instructions = get_instruction_set(input)
    initialize_register(registers0, instructions, 0)
    initialize_register(registers1, instructions, 1)
    (ip0, ip1) = (0, 0)
    q0 = queue.Queue()
    q1 = queue.Queue()

    program1_messages_count = 0
    while True:
        is_deadlocked = False
        is_halted = True
        # program 0
        while True:
            if ip0 >= 0 and ip0 < len(instructions):
                is_halted = False
                instruction = instructions[ip0]
                if instruction.op == 'rcv' and q0.empty():
                    break
                ip0 += executePartTwo(instruction, registers0, q1, q0)
        
        # program 1
        while True:
            if ip1 >= 0 and ip1 < len(instructions):
                is_halted = False
                instruction = instructions[ip1]
                if instruction.op == 'rcv' and q1.empty():
                    break
                if instruction.op == 'snd':
                    program1_messages_count += 1
                ip1 += executePartTwo(instruction, registers1, q0, q1)

        if q0.empty() and q1.empty():
            # print("Program is deadlocked")
            break
        if is_halted:
            # print("Program has reached the end. Terminating...")
            break

    return program1_messages_count

 
def executePartOne(ins, registers):
    if ins.op == 'snd':
        registers['snd'] = get_value(ins.x, ins.x_mode, registers)
    elif ins.op == 'set':
        registers[ins.x] = get_value(ins.y, ins.y_mode, registers)
    elif ins.op == 'add':
        registers[ins.x] += get_value(ins.y, ins.y_mode, registers)
    elif ins.op == 'mul':
        registers[ins.x] *= get_value(ins.y, ins.y_mode, registers)
    elif ins.op == 'mod':
        registers[ins.x] %= get_value(ins.y, ins.y_mode, registers)
    elif ins.op == 'rcv':
        x = get_value(ins.x, ins.x_mode, registers)
        if x > 0:
            registers['rcv'] = registers['snd']
    elif ins.op == 'jgz':
        x = get_value(ins.x, ins.x_mode, registers)
        if x > 0:
            return get_value(ins.y, ins.y_mode, registers)
    else:
        assert False, f"Unknown instruction: {ins}"

    return 1

def executePartTwo(ins, registers, send, receive):
    if ins.op == 'snd':
        x = get_value(ins.x, ins.x_mode, registers)
        send.put(x)
    elif ins.op == 'set':
        registers[ins.x] = get_value(ins.y, ins.y_mode, registers)
    elif ins.op == 'add':
        registers[ins.x] += get_value(ins.y, ins.y_mode, registers)
    elif ins.op == 'mul':
        registers[ins.x] *= get_value(ins.y, ins.y_mode, registers)
    elif ins.op == 'mod':
        registers[ins.x] %= get_value(ins.y, ins.y_mode, registers)
    elif ins.op == 'rcv':
        if not receive.empty():
            registers[ins.x] = receive.get()
        else:
            return 0
    elif ins.op == 'jgz':
        x = get_value(ins.x, ins.x_mode, registers)
        if x > 0:
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

def initialize_register(registers, instructions, p_register):
    for ins in instructions:
        registers[ins.x] = 0
    registers['p'] = p_register


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
