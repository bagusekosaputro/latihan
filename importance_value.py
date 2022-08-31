def sum_importance_value(employees: list, employee_id: int):
    importance_value = 0

    for employee in employees:
        if employee_id == employee[0]:
            subordinates = employee[2]
            for subordinate in subordinates:
                importance_value += sum_importance_value(employees, subordinate)
            importance_value += employee[1]
            break

    return importance_value

if __name__ == "__main__":
    employee_id = 1
    # employees = [[1,5,[2,3]], [2,3,[]], [3,3,[]]]
    employees = [[1,5,[2]], [2,3,[3]], [3,3,[]]]
    result = sum_importance_value(employees, employee_id)

    print(f"Importance value: {result}")


