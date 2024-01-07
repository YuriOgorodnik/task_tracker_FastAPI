from httpx import AsyncClient


async def test_create_employee(ac: AsyncClient):
    response = await ac.post(
        "/employee/create",
        json={
            "last_name": "Петров",
            "first_name": "Петр",
            "patronymic": "Петрович",
            "position": "Инженер",
            "phone_number": "+375442135648",
            "email": "petrovpetr@gmail.com",
            "address": "улица Советская, 11-22",
            "city": "город Бобруйск",
            "country": "Республика Беларусь",
        },
    )

    assert response.status_code == 200


async def test_create_task(ac: AsyncClient):
    response = await ac.post(
        "/task/create",
        json={
            "title": "Провести вводный инструктаж",
            "created_at": "2024-01-06T21:26:28",
            "deadline": "2024-01-12T21:26:28",
            "is_active": True,
            "employee_id": 2,
        },
    )

    assert response.status_code == 200


async def test_get_task(ac: AsyncClient):
    response = await ac.get("/task/get/1")
    assert response.status_code == 200
    task = response.json()
    assert task["id"] == 1


async def test_list_tasks(ac: AsyncClient):
    response = await ac.get("/task/list")
    assert response.status_code == 200


async def test_update_task(ac: AsyncClient):
    updated_task = {
        "id": 1,
        "title": "Обновленная задача",
        "created_at": "2024-01-06T21:26:28",
        "deadline": "2024-01-12T21:26:28",
        "is_active": True,
        "employee_id": 2,
    }

    response = await ac.put("/task/update/1", json=updated_task)

    assert response.status_code == 200
    updated_task = response.json()
    assert updated_task["title"] == "Обновленная задача"


async def test_delete_task(ac: AsyncClient):
    response = await ac.delete("/task/delete/1")
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "success"


async def test_important_tasks(ac: AsyncClient):
    response = await ac.get("task/important_tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    for task in response.json():
        assert isinstance(task, dict)
        assert "important_task" in task
        assert isinstance(task["important_task"], dict)
        assert "id" in task["important_task"]
        assert "title" in task["important_task"]
        assert "deadline" in task["important_task"]
        assert "is_active" in task["important_task"]
        assert "eligible_employees" in task["important_task"]
