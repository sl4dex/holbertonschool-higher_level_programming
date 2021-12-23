#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv, exit
    if len(argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if argv[2] == "+":
            print("{} + {} = {}".format(
                argv[1], argv[3],
                calc.add(int(argv[1]), int(argv[3]))))
        elif argv[2] == "-":
            print("{} - {} = {}".format(
                argv[1], argv[3],
                calc.sub(int(argv[1]), int(argv[3]))))
        elif argv[2] == "*":
            print("{} * {} = {}".format(
                argv[1], argv[3],
                calc.mul(int(argv[1]), int(argv[3]))))
        elif argv[2] == "/":
            print("{} / {} = {}".format(
                argv[1], argv[3],
                calc.div(int(argv[1]), int(argv[3]))))
