def print_hi(name):
    print(f'Hi, {name}')


def operatestuff(fuckthisregup: (str, int), opera: str, value: int):
    if opera == "add":
        fuckthisregup[1] += value
        print("adding")
        print(fuckthisregup)
    elif opera == "sub":
        fuckthisregup[1] -= value
        print("sub")
        print(fuckthisregup)
    elif opera == "mult":
        fuckthisregup[1] *= value
        print("mult")
        print(fuckthisregup)
    elif opera == "div":
        if value == 0:
            print("DIE YOU SHIT")
            return False
        else:
            fuckthisregup[1] /= value
            print("mult")
            print(fuckthisregup)
    else:
        print("fuck no")
    return True


registers: (str, int) = []
knownRegisters = []
knownOperations = ["add", "sub", "mult", "div"]


if __name__ == '__main__':
    print_hi('you fucking nerd..')

    while True:
        inp = input("enter stuff: ")
        if inp.lower() == "quit":
            break

        splitString = inp.split(" ", 3)

        if splitString[0] == "print":
            regtoprint = splitString[1]
            if regtoprint == "all":
                for register in registers:
                    print(register)
            elif regtoprint not in knownRegisters:
                print("there is no fucking register you shit")
                break
            else:
                for register in registers:
                    if regtoprint == register[0]:
                        print(register)
        else:
            if len(splitString) < 3:
                print("you are an idiot")
                break
            else:
                reg = splitString[0]
                op = splitString[1]
                val = splitString[2]
                numval = 0

                if op not in knownOperations:
                    print("fuck off, unknown operation dumbass")
                    break

                if not val.isnumeric():
                    if val in knownRegisters:
                        for register in registers:
                            if val == register[0]:
                                numval = register[1]
                    else:
                        print("shit, that's not a number")
                        break
                else:
                    numval = int(val)
                if reg in knownRegisters:
                    for register in registers:
                        if splitString[0] == register[0]:
                            if not operatestuff(register, op, numval):
                                break
                else:
                    knownRegisters.append(reg)
                    newreg = [reg, 0]
                    registers.append(newreg)
                    if not operatestuff(newreg, op, numval):
                        break


print("quiting this shit")
for register in registers:
    reg = register[0]
    val = register[1]
    print(reg + ": " + str(val))
