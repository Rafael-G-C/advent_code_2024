import re

total = 0

def multiplier(args):
    sub_total = 0
    for arg in args:
        sub_total += int(arg[0]) * int(arg[1])
    return sub_total
    l
with open("input", "r") as file:
    lines = file.readlines()

    for line in lines:
        found = re.findall("mul\((\d+)\,(\d+)\)",line)
        total += multiplier(found)
    print(total)