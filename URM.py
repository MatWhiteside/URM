import sys

""""
Program to model a URM as given from "CS-275: Automata and Formal Language Theory" module @ Swansea University.
Author: Matthew Whiteside

Instructions:
 - Rk := Rk + 1
 - Rk := Rk - 1
 - if Rk = 0 then goto q
 - stop: finished entering instructions (only applies to console)
"""


registers = []
org_instructions = []
instructions = []
pc = 0


"""
    Initialise the URM by setting all registers to 0 and then loading in
    the given inputs.
"""
def init_urm(num_registers, inputs):
    # Set n registers to 0 where n = num_registers
    for i in range(0, num_registers):
        registers.append(0)

    # Load the inputs into the registers
    for input_num in range(len(inputs)):
        registers[input_num] = int(inputs[input_num])


"""
    Adds an instruction to the URM, used during the input process.
"""
def add_instruction(instruction):
    global instructions, org_instructions
    instructions.append(instruction)
    org_instructions.append(instruction)


"""
    Processes a given file containing a URM program, each instruction should be on a new line.
"""
def file_in(file_path):
    # Read in each line and remove the newline character
    lines = [line.strip('\n') for line in open(file_path)]

    # For each line read in, add it to the instructions
    for l in lines:
        add_instruction(l)


"""
    Takes the program from the console instead of from a file.
"""
def console_in():
    # Take the program as an input via the console
    ins = input("Enter instruction: ")
    while ins != "stop":
        add_instruction(ins)
        ins = input("Enter instruction: ")


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


"""
    Converts a register "Rk" to an index value k.
"""
def register_to_index(register):
    return int(register[-1:])


"""
    Executes the URM once the intructions, and inputs have been loaded in.
"""
def run_urm():
    global instructions, registers, pc

    # While the program isn't finished executing
    while pc < len(instructions):
        pc_changed = False  # True if a goto statement executes

        # Fetches the already encoded instruction to execute and splits it up
        # into instruction and register.
        cur_instruction_list = instructions[pc]
        cur_instruction = cur_instruction_list[0]
        cur_register = cur_instruction_list[1]

        # Execute the instructions
        if cur_instruction == "s":
            registers[cur_register] = registers[cur_register] + 1
        elif cur_instruction == "p":
            registers[cur_register] = registers[cur_register] - 1
        elif cur_instruction == "goto":
            # Condition is true, so print the state then change the PC
            if registers[cur_register] == 0:
                print_state()
                pc = cur_instruction_list[2]
                pc_changed = True

        # If the PC hasn't been changed by a goto statement, increment it
        if not pc_changed:
            print_state()
            pc += 1


"""
    Prints the value of the PC, registers and the instruction just executed. Strips off the excess registers where
    values are 0.
"""
def print_state():
    # Make sure program hasn't finished executing
    if pc < len(org_instructions):
        # Find the last register in the list that is being used, going backwards through the list
        # to detect this
        end_reg = len(registers)
        for elem in reversed(registers):
            if elem != 0:
                break
            end_reg -= 1
        # If all the registers are 0, show R0 only
        if end_reg == 0:
            end_reg = 1

        print("PC: {} Registers: {} Executed: '{}'".format(pc, registers[:end_reg], org_instructions[pc]))


"""
    Entry points for the application. Takes instructions, inputs, initialises the URM, encodes instructions
    and then executes the URM.
"""
if __name__ == '__main__':
    file_in("URMProgram.txt")

    parameters = []
    # Take the inputs via the console
    param = input("Enter parameter: ")
    while param != "stop":
        parameters.append(param)
        param = input("Enter parameter: ")

    # Initialise 100 registers, should be sufficient for smaller URM programs
    init_urm(100, parameters)

    # Encode instructions for processing
    encode_instructions()

    # Execute the URM
    run_urm()
