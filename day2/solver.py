from pprint import pprint

# with open("./day2/input-test.txt", "r") as fp:
with open("./day2/input-challange.txt", "r") as fp:
    reports = []
    for line in fp.readlines():
        reports.append([int(x) for x in line.split()])


def is_safe(report: []) -> bool:
    increasing = report[0] < report[1]
    for i in range((len(report)-1)):
        # Unsafe if increasing and we find descreasing pairs
        if increasing and report[i] > report[i+1]:
            return False
        # Unsafe if decreasing and we find increasing pair
        if not increasing and report[i] < report[i+1]:
            return False
        diff = abs(report[i]-report[i+1])
        # Unsafe if numbers don't differ
        if diff == 0:
            return False
        # Unsafe if numbers differ by more than 3
        if diff > 3:
            return False
    return True

def is_safe_with_skip(report: []) -> bool:
    for n in range(len(report)):
        run_copy_report = report.copy()
        del run_copy_report[n]

        run_is_safe = True

        increasing = run_copy_report[0] < run_copy_report[1]
        for i in range((len(run_copy_report)-1)):
            # Unsafe if increasing and we find descreasing pairs
            if increasing and run_copy_report[i] > run_copy_report[i+1]:
                run_is_safe = False
                break
            # Unsafe if decreasing and we find increasing pair
            if not increasing and run_copy_report[i] < run_copy_report[i+1]:
                run_is_safe = False
                break
            diff = abs(run_copy_report[i]-run_copy_report[i+1])
            # Unsafe if numbers don't differ
            if diff == 0:
                run_is_safe = False
                break
            # Unsafe if numbers differ by more than 3
            if diff > 3:
                run_is_safe = False
                break
        if run_is_safe:
            return True


count = 0
for report in reports:
    print(report)
    if is_safe(report):
    # if is_safe_with_skip(report):
        count += 1
        print("Safe")
    else:
        print("Unsafe")

print(f"safe reports: {count}")