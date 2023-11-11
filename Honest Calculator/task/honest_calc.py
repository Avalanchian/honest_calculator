def calculate(inputs: dict) -> float:
    x: float = inputs['x']
    y: float = inputs['y']
    operation: str = inputs['operation']
    match operation:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y


def save_result(result: float, memory: float) -> float:
    msg_4: str = "Do you want to store the result? (y / n):"
    msgs = [
        "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"
    ]

    while True:
        print(msg_4)
        answer = input()
        if answer != 'y' and answer != 'n':
            continue
        if answer == 'n':
            return memory
        if answer == 'y' and not is_one_digit(result):
            memory = result
            return memory
        index = 0
        while index < 3:
            print(msgs[index])
            answer = input()
            if answer != 'y' and answer != 'n':
                continue
            if answer == 'n':
                return memory
            index += 1
        memory = result
        return memory


def continue_calculating() -> bool:
    msg_5: str = "Do you want to continue calculations? (y / n):"
    while True:
        print(msg_5)
        answer = input()
        if answer != 'y' and answer != 'n':
            continue
        if answer == 'y':
            return True
        return False


def is_one_digit(num: float) -> bool:
    if num.is_integer() and -10 < num < 10:
        return True
    return False


def lazy_check(inputs: dict):
    x: float = inputs['x']
    y: float = inputs['y']
    operation: str = inputs['operation']
    msg: str = ""
    msg_6: str = " ... lazy"
    msg_7: str = " ... very lazy"
    msg_8: str = " ... very, very lazy"
    msg_9: str = "You are"
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if x == 1 or y == 1 and operation == '*':
        msg += msg_7
    if x == 0 or y == 0 and (operation in ('*', '+', '-')):
        msg += msg_8
    if msg != "":
        print(msg_9 + msg)


def main():
    msg_0: str = "Enter an equation"
    msg_1: str = "Do you even know what numbers are? Stay focused!"
    msg_2: str = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    msg_3: str = "Yeah... division by zero. Smart move..."

    memory: float = 0.0

    while True:
        print(msg_0)
        calc: str = input().strip()
        if len(calc.split()) != 3:
            return
        try:
            inputs: dict = {'x': float(calc.split()[0]), 'operation': calc.split()[1], 'y': float(calc.split()[2])}
        except ValueError:
            if calc.split()[0] == 'M' and calc.split()[2] == 'M':
                inputs: dict = {'x': memory, 'operation': calc.split()[1], 'y': memory}
            elif calc.split()[0] == 'M':
                inputs: dict = {'x': memory, 'operation': calc.split()[1], 'y': float(calc.split()[2])}
            elif calc.split()[2] == 'M':
                inputs: dict = {'x': float(calc.split()[0]), 'operation': calc.split()[1], 'y': memory}
            else:
                print(msg_1)
                continue

        if inputs['operation'] not in ('+', '-', '*', '/'):
            print(msg_2)
            continue

        lazy_check(inputs)

        if inputs['operation'] == '/' and inputs['y'] == 0:
            print(msg_3)
            continue

        result: float = calculate(inputs)
        print(result)

        memory: float = save_result(result, memory)

        if continue_calculating():
            continue
        else:
            break


if __name__ == '__main__':
    main()
