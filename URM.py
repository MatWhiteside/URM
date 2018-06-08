""""
Instructions:
 - Rk := Rk + 1
 - Rk := Rk - 1
 - if B then goto q
 - stop: finished entering instructions
"""



registers = []
instructions = []
PC = 0


def add_instruction(instruction):
    global instructions
    instructions.append(instruction)


if __name__ == '__main__':
    ins = input("Enter instruction: ")

    while ins != "stop":
        add_instruction(ins)
        ins = input("Enter instruction: ")


