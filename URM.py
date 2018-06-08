import sys

""""
Instructions:
 - Rk := Rk + 1
 - Rk := Rk - 1
 - if Rk = 0 then goto q
 - stop: finished entering instructions
"""


registers = []
org_instructions = []
instructions = []
pc = 0


def init_urm(num_registers, inputs):
    # Set n registers to 0 where n = num_registers
    for i in range(0, num_registers):
        registers.append(0)

    # Load the inputs into the registers
    for input_num in range(len(inputs)):
        registers[input_num] = int(inputs[input_num])


def add_instruction(instruction):
    global instructions, org_instructions
    instructions.append(instruction)
    org_instructions.append(instruction)


"""
Encodes instructions so they can be executed:
 - Successor: [s, reg#]
 - Predecessor: [p, reg#]
 - Cond. goto: [goto, reg#, ins#]
"""
def encode_instructions():
    global instructions

    for input_num in range(len(instructions)):
        # Fetch the instruction to encode
        ins_to_process = instructions[input_num]

        # Encode the instruction
        if "+" in ins_to_process:       # Successor
            instructions[input_num] = ["s", register_to_index(ins_to_process[0:ins_to_process.find(" ")])]
        elif "-" in ins_to_process:     # Predecessor
            instructions[input_num] = ["p", register_to_index(ins_to_process[0:ins_to_process.find(" ")])]
        elif "goto" in ins_to_process:  # Conditional goto
            instructions[input_num] = [
                "goto",
                register_to_index(ins_to_process[ins_to_process.find("R")+1:ins_to_process.find(" =")]),
                int(ins_to_process[-ins_to_process[::-1].find(" "):])
            ]
        else:
            print("Invalid instruction: " + ins_to_process)
            sys.exit(0)


def register_to_index(register):
    return int(register[-1:])


def run_urm():
    global instructions, registers, pc

    while pc < len(instructions):
        pc_changed = False

        cur_instruction_list = instructions[pc]
        cur_instruction = cur_instruction_list[0]
        cur_register = cur_instruction_list[1]

        if cur_instruction == "s":
            registers[cur_register] = registers[cur_register] + 1
        elif cur_instruction == "p":
            registers[cur_register] = registers[cur_register] - 1
        elif cur_instruction == "goto":
            if registers[cur_register] == 0:
                print_registers()
                pc = cur_instruction_list[2]
                pc_changed = True

        if not pc_changed:
            print_registers()
            pc += 1


def print_registers():
    if pc < len(org_instructions):
        end_reg = len(registers)
        for elem in reversed(registers):
            if elem != 0:
                break
            end_reg -= 1
        if end_reg == 0:
            end_reg = 1

        print("PC: {} Registers: {} Executed: '{}'".format(pc, registers[:end_reg], org_instructions[pc]))


if __name__ == '__main__':
    # Take the program as an input via the console
    ins = input("Enter instruction: ")
    while ins != "stop":
        add_instruction(ins)
        ins = input("Enter instruction: ")

    parameters = []
    # Take the inputs via the console
    param = input("Enter parameter: ")
    while param != "stop":
        parameters.append(param)
        param = input("Enter parameter: ")

    # Initialise 100 registers, should be sufficient for smaller URM programs
    init_urm(100, parameters)

    encode_instructions()

    run_urm()
