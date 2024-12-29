import re
from pprint import pprint

# with open("./day3/input-test-part2.txt", "r") as fp:
with open("./day3/input-challange.txt", "r") as fp:
    memory = []
    for line in fp.readlines():
        memory.append(line)

# pprint(memory)

re_mul = re.compile(r"(mul\((\d{1,3})\,(\d{1,3})\))|(don\'t\(\)|do\(\))")

res = 0
add = True
for line in memory:
    if match := re_mul.findall(line):
        pprint(match)
        for _, x, y, do_nt in match:
            if x and y and add:
                res += int(x) * int(y)
            elif do_nt:
                if do_nt == "don't()":
                    add = False
                elif do_nt =="do()":
                    add = True


print(res)

# print(matches.group())