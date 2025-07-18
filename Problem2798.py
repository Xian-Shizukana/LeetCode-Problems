def numberOfEmployeesWhoMetTarget(hours:list[int], target: int) -> int:
    good_employees = 0

    for i in hours:
        if i >= target:
            good_employees += 1

    return good_employees

print(numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))
