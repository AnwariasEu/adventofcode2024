import json
from pprint import pprint

# with open("./day1/input-test.txt", "r") as fp:
#     list1 = []
#     list2 = []
#     for line in fp.readlines():
#         x, y = line.split()
#         list1.append(int(x))
#         list2.append(int(y))

with open("./day1/input-challange.txt", "r") as fp:
    list1 = []
    list2 = []
    for line in fp.readlines():
        x, y = line.split()
        list1.append(int(x))
        list2.append(int(y))
    

# pprint(list1)
# pprint(list2)

# Requires sorted lists as input
def get_total_distance(list1 :[], list2 :[]) -> int:
    assert len(list1) == len(list2)
    dist = 0 
    for i in range(0,len(list1)):
        dist += abs(list1[i]-list2[i])
    return dist


# list can be sorted or not (shrug), count in for loop is O(N) * O(N) not nice but works
def get_similarity_score(list1: [], list2: []) -> int:
    score = 0
    for i in list1:
        score += i * list2.count(i)
    return score


total_distance = get_total_distance(sorted(list1), sorted(list2))
print(f"total distance: {total_distance}")
score = get_similarity_score(list1, list2)
print(f"similarity score: {score}")