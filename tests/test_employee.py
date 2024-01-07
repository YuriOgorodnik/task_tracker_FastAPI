from httpx import AsyncClient


async def test_create_employee(ac: AsyncClient):
    response = await ac.post(
        "/employee/create",
        json={
            "last_name": "Иванов",
            "first_name": "Иван",
            "patronymic": "Иванович",
            "position": "Инженер по охране труда",
            "phone_number": "+375443254618",
            "email": "ivanovivan@gmail.com",
            "address": "улица Строителей, 27-17",
            "city": "город Бобруйск",
            "country": "Республика Беларусь",
        },
    )

    assert response.status_code == 200


async def test_get_employee(ac: AsyncClient):
    response = await ac.get("/employee/get/1")
    assert response.status_code == 200
    employee = response.json()
    assert employee["id"] == 1


async def test_list_employees(ac: AsyncClient):
    response = await ac.get("/employee/list")
    assert response.status_code == 200


async def test_update_employee(ac: AsyncClient):
    update_data = {
        "first_name": "Новое_имя",
        "last_name": "Новая_фамилия",
        "position": "Новая_должность",
    }

    response = await ac.put("/employee/update/1", json=update_data)

    assert response.status_code == 200
    updated_employee = response.json()
    assert updated_employee["first_name"] == "Новое_имя"
    assert updated_employee["last_name"] == "Новая_фамилия"
    assert updated_employee["position"] == "Новая_должность"


async def test_delete_employee(ac: AsyncClient):
    response = await ac.delete("/employee/delete/1")
    assert response.status_code == 200
    result = response.json()
    assert result["message"] == "Employee deleted successfully"


async def test_busy_employees(ac: AsyncClient):
    response = await ac.get("/employee/busy_employees")
    assert response.status_code == 200
    employees_with_tasks = response.json()
    for employee in employees_with_tasks:
        assert "employee" in employee
        assert "last_name" in employee
        assert "first_name" in employee
        assert "patronymic" in employee
        assert "position" in employee
        assert "active_tasks_count" in employee
