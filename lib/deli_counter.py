def line(line):
    if len(line) == 0:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for ind, name in enumerate(line):
            message += f" {ind+1}. {name}"
        print(message)


def take_a_number(line, newL):
    line.append(newL)
    print(f"Welcome, {newL}. You are number {len(line)} in line.")
    pass


def now_serving(line):
    if len(line):
        print(f"Currently serving {line[0]}.")
        line.pop(0)
    else:
        print("There is nobody waiting to be served!")
    pass
