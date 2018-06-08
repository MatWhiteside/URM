""""
Instructions:
 - Rk := Rk + 1
 - Rk := Rk - 1
 - if B then goto q
 - stop: finished entering instructions
"""


registers = []
instructions = []
pc = 0


def init_urm(num_registers, inputs):
    # Set n registers to 0 where n = num_registers
    for i in range(0, num_registers):
        registers.append(0)

    # Load the inputs into the registers
    for input_num in range(len(inputs)):
        registers[input_num] = inputs[input_num]


def add_instruction(instruction):
    global instructions
    instructions.append(instruction)


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