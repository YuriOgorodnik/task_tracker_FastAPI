from src.employee.dao import EmployeeDAO
from src.task.dao import TaskDAO


async def get_eligible_employees(session, task_id):
    # Получаем информацию о задаче
    task_info = await TaskDAO.get_task_by_id(session, task_id)
    if task_info is None:
        return []

    # Извлекаем данные о задаче.
    (
        task_id,
        title,
        created_at,
        deadline,
        is_active,
        parent_task_id,
        employee_id,
    ) = task_info

    # Если у задачи есть родительская задача, находим информацию о ней
    parent_task_info = (
        await TaskDAO.get_task_by_id(session, parent_task_id)
        if parent_task_id
        else None
    )
    parent_employee_id = parent_task_info[6] if parent_task_info else None

    # Получаем всех сотрудников, отсортированных по количеству задач
    all_employees = await EmployeeDAO.get_all_employees(session)

    # Находим наименее загруженного сотрудника
    sorted_employees = sorted(all_employees, key=lambda x: len(x[9]))
    least_loaded_employee = sorted_employees[0] if sorted_employees else None

    eligible_employees = []

    # Проверяем, соответствует ли наименее загруженный сотрудник критериям
    if least_loaded_employee:
        least_loaded_employee_task_count = len(least_loaded_employee[9])
        if (not parent_employee_id) or least_loaded_employee_task_count <= (
            len(parent_task_info[9]) + 2
        ):
            # Создаем объект с информацией о задаче и сотруднике
            eligible_employees.append(
                f"{least_loaded_employee[1]} {least_loaded_employee[2]} {least_loaded_employee[3]}"
            )

    return eligible_employees
