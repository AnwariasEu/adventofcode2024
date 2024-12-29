import re
from pprint import pprint

# with open("./day3/input-test.txt", "r") as fp:
with open("./day3/input-challange.txt", "r") as fp:
    memory = []
    for line in fp.readlines():
        memory.append(line)

# pprint(memory)

re_mul = re.compile(r"mul\((\d{1,3})\,(\d{1,3})\)")

res = 0
for line in memory:
    if match := re_mul.findall(line):
        pprint(match)
        for x, y in match:
            res += int(x) * int(y)

print(res)

# print(matches.group())
